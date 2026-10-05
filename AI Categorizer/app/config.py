"""
Application configuration.
"""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    Application settings.
    """

    gemini_api_key: str
    gemini_model: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()