"""Configuration settings for the FastAPI application."""

from pydantic_settings import BaseSettings  # type: ignore


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "FastAPI Sample"
    DEBUG: bool = False
    API_PREFIX: str = ""

    class Config:
        """Pydantic config class for Settings."""

        env_file = ".env"


settings = Settings()
