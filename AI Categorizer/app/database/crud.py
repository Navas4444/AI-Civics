"""
CRUD operations.
"""

import uuid

from sqlalchemy.orm import Session

from app.database.models import Complaint


def get_all_complaints(db: Session):
    """
    Return all complaints ordered by newest first.
    """

    return (
        db.query(Complaint)
        .order_by(Complaint.created_at.desc())
        .all()
    )


def update_complaint_status(
    db: Session,
    complaint_id: str,
    status: str,
):
    """
    Update complaint status.
    """

    complaint = (
        db.query(Complaint)
        .filter(
            Complaint.complaint_id == complaint_id
        )
        .first()
    )

    if complaint is None:
        return None

    complaint.status = status

    db.commit()
    db.refresh(complaint)

    return complaint


def create_complaint(
    db: Session,
    result: dict,
    description: str,
    image_path: str | None,
):
    """
    Save complaint to database.
    """

    location = result.get("location") or {}

    complaint = Complaint(
        complaint_id=f"CMP-{uuid.uuid4().hex[:8].upper()}",
        description=description,
        image_path=image_path,

        latitude=location.get("latitude"),
        longitude=location.get("longitude"),
        place_name=location.get("place_name"),
        address=location.get("address"),
        city=location.get("city"),
        district=location.get("district"),
        state=location.get("state"),
        country=location.get("country"),
        postal_code=location.get("postal_code"),

        department=result["department"],
        subcategory=result["subcategory"],
        priority=result["priority"],
        confidence=result["confidence"],
        reason=result["reason"],
        human_review=result["human_review"],
    )

    db.add(complaint)
    db.commit()
    db.refresh(complaint)

    return complaint