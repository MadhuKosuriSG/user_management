"""Configuration settings for the FastAPI application."""

import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "FastAPI Sample"
    APP_NAME: str = "FastAPI Sample"
    DEBUG: bool = False
    API_PREFIX: str = ""
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")  # Default SQLite database URL

    # Database settings
    DATABASE_USER: str = "root"
    DATABASE_PASSWORD: str = ""
    DATABASE_HOST: str = "db"
    DATABASE_PORT: str = "3306"
    DATABASE_NAME: str = "bookmyshow_development"

    # Uvicorn settings
    UVICORN_RELOAD: str = "true"
    UVICORN_HOST: str = "0.0.0.0"
    UVICORN_PORT: str = "8000"

    class Config:
        """Pydantic config class for Settings."""

        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Ignore extra fields from .env


# Create settings instance
settings = Settings()
