"""
Gemini AI client.

This module is responsible for communicating with
Google Gemini.
"""

from google import genai

from app.config import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def test_connection():
    """
    Send a simple prompt to verify that
    Gemini is working correctly.
    """

    prompt = (
        "Reply with exactly these words: "
        "Gemini connection successful."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text