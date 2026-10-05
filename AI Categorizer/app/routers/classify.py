"""
Complaint Classification Router
"""

import os
import uuid
from pathlib import Path
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database.database import get_db
from app.database.crud import create_complaint
from fastapi import (
    APIRouter,
    File,
    Form,
    HTTPException,
    UploadFile,
)
from PIL import Image
from fastapi import Request
from app.limiter import limiter
from app.schemas.response import ClassificationResponse
from app.services.classifier_service import classifier_service

router = APIRouter(
    prefix="/classify",
    tags=["AI Classifier"],
)

UPLOAD_FOLDER = "uploads"

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".bmp",
    ".heic",
}

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True,
)


@router.post(
    "",
    response_model=ClassificationResponse,
)
@limiter.limit("20/minute")
async def classify_complaint(
    request: Request,
    db: Session = Depends(get_db),
    description: str = Form(...),
    latitude: float | None = Form(None),
    longitude: float | None = Form(None),
    image: UploadFile | None = File(None),
):
    """
    Classify a civic complaint.
    """

    image_path = None

    try:

        if image is not None:

            extension = Path(
                image.filename
            ).suffix.lower()

            if extension not in ALLOWED_EXTENSIONS:
                raise HTTPException(
                    status_code=400,
                    detail=(
                        "Unsupported image format. "
                        "Allowed formats are JPG, JPEG, PNG, "
                        "WEBP, BMP and HEIC."
                    ),
                )

            content = await image.read()

            if len(content) > MAX_IMAGE_SIZE:
                raise HTTPException(
                    status_code=400,
                    detail="Image size must be under 10 MB.",
                )

            filename = (
                f"{uuid.uuid4()}"
                f"{extension}"
            )

            image_path = os.path.join(
                UPLOAD_FOLDER,
                filename,
            )

            with open(
                image_path,
                "wb",
            ) as file:

                file.write(content)

            try:

                img = Image.open(
                    image_path
                )

                img.verify()

            except Exception:

                if os.path.exists(image_path):
                    os.remove(image_path)

                raise HTTPException(
                    status_code=400,
                    detail="Invalid or corrupted image.",
                )

        result = classifier_service.classify(
            description=description,
            latitude=latitude,
            longitude=longitude,
            image_path=image_path,
        )
        create_complaint(
            db=db,
            result=result,
            description=description,
            image_path=image_path,
        )
        return ClassificationResponse(
            **result
        )

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc

# Keep uploaded images for the Admin Dashboard.
# We'll delete them only if the complaint is removed.
