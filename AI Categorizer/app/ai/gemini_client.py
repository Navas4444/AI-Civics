"""
Gemini AI Client
"""

import json

from json import JSONDecodeError
from pathlib import Path

from google import genai
from google.genai import types

from app.utils import reverse_geocode
from app.config import settings
from app.prompts import build_classification_prompt


class GeminiClient:
    """
    Handles communication with Gemini.
    """

    def __init__(self) -> None:
        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

        self.model = settings.gemini_model

    def classify(
        self,
        description: str,
        latitude: float | None = None,
        longitude: float | None = None,
        image_path: str | None = None,
    ) -> dict:
        """
        Classify a civic complaint.
        """
        location = "Location not provided"

        if latitude is not None and longitude is not None:
            location = reverse_geocode(
                latitude,
                longitude,
            )

        prompt = build_classification_prompt(
            description=description,
            latitude=latitude,
            longitude=longitude,
            location=location,
        )

        contents = [prompt]

        if image_path:
            image = Path(image_path)

            contents.append(
                types.Part.from_bytes(
                    data=image.read_bytes(),
                    mime_type="image/jpeg",
                )
            )

        response = self.client.models.generate_content(
            model=self.model,
            contents=contents,
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        try:
            result = json.loads(text)

        except JSONDecodeError as exc:
            raise ValueError("Gemini returned invalid JSON.") from exc

        required_fields = [
            "department",
            "subcategory",
            "priority",
            "confidence",
            "reason",
            "human_review",
        ]

        missing = [field for field in required_fields if field not in result]

        if missing:
            raise ValueError(f"Missing fields from Gemini response: {missing}")

        if not isinstance(result["confidence"], int):
            raise ValueError("Confidence must be an integer.")

        if result["confidence"] < 0 or result["confidence"] > 100:
            raise ValueError("Confidence must be between 0 and 100.")

        return result