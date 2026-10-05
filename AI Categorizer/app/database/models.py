"""
Database models.
"""

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.database.database import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(String, unique=True, index=True)

    description = Column(String, nullable=False)

    image_path = Column(String, nullable=True)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    place_name = Column(String, nullable=True)

    address = Column(String, nullable=True)

    city = Column(String, nullable=True)

    district = Column(String, nullable=True)

    state = Column(String, nullable=True)

    country = Column(String, nullable=True)

    postal_code = Column(String, nullable=True)

    department = Column(String, nullable=False)

    subcategory = Column(String, nullable=False)

    priority = Column(String, nullable=False)

    confidence = Column(Integer, nullable=False)

    reason = Column(String, nullable=False)

    human_review = Column(Boolean, default=False)

    status = Column(String, default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )