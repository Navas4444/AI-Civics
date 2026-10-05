"""
Complaint Router
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.crud import update_complaint_status
from app.database.database import get_db
from app.database.crud import get_all_complaints

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"],
)


@router.patch("/{complaint_id}/status")
def change_status(
    complaint_id: str,
    status: str,
    db: Session = Depends(get_db),
):

    complaint = update_complaint_status(
        db,
        complaint_id,
        status,
    )

    if complaint is None:

        raise HTTPException(
            status_code=404,
            detail="Complaint not found",
        )

    return {
        "message": "Status updated successfully."
    }


@router.get("")
def list_complaints(
    db: Session = Depends(get_db),
):
    return get_all_complaints(db)