"""Main application module for FastAPI app."""

from fastapi import FastAPI

from app.core.api_router import router
from app.core.config import settings
from app.db.session import Base, engine


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title=settings.PROJECT_NAME)

    # include main router
    app.include_router(router)

    # dev convenience: create tables automatically (not for prod)
    @app.on_event("startup")
    def on_startup() -> None:
        """Create database tables on startup."""
        Base.metadata.create_all(bind=engine)

    return app


app = create_app()
