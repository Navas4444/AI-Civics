"""
Classifier Service
"""

from app.ai.gemini_client import GeminiClient


class ClassifierService:
    """
    Handles complaint classification.
    """

    def __init__(self) -> None:
        self.client = GeminiClient()

    def classify(
        self,
        description: str,
        latitude: float,
        longitude: float,
        image_path: str | None = None,
    ) -> dict:
        """
        Classify a complaint using Gemini.
        """

        result = self.client.classify(
            description=description,
            latitude=latitude,
            longitude=longitude,
            image_path=image_path,
        )

        return result


classifier_service = ClassifierService()