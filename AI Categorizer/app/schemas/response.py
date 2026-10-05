"""
Response schema for complaint classification.
"""

from typing import Optional

from pydantic import BaseModel, Field


class LocationResponse(BaseModel):
    """
    Complaint location details.
    """

    latitude: float

    longitude: float

    place_name: Optional[str] = None

    address: Optional[str] = None

    city: Optional[str] = None

    district: Optional[str] = None

    state: Optional[str] = None

    country: Optional[str] = None

    postal_code: Optional[str] = None

    google_maps_url: Optional[str] = None


class ClassificationResponse(BaseModel):
    """
    Response returned by the AI classifier.
    """

    department: str = Field(
        ...,
        description="Government department responsible.",
    )

    subcategory: str = Field(
        ...,
        description="Specific complaint category.",
    )

    priority: str = Field(
        ...,
        description="Complaint priority.",
    )

    confidence: int = Field(
        ...,
        ge=0,
        le=100,
        description="AI confidence score.",
    )

    reason: str = Field(
        ...,
        description="Reason for classification.",
    )

    human_review: bool = Field(
        ...,
        description="Whether manual review is recommended.",
    )

    location: Optional[LocationResponse] = Field(
        default=None,
        description="Complaint location details.",
    )