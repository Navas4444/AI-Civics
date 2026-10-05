"""
Request schema.
"""

from pydantic import BaseModel, Field


class ComplaintRequest(BaseModel):
    description: str = Field(
        ...,
        min_length=3,
        max_length=5000,
    )

    latitude: float | None = None

    longitude: float | None = None