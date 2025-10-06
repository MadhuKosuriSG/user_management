"""Health check endpoint for application monitoring."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check() -> dict[str, str]:
    """Return health status."""
    return {"status": "healthy"}
