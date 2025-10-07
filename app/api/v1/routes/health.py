"""Health check endpoint for application monitoring."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()


@router.get("")
def health_check() -> dict[str, str]:
    """Return health status."""
    return {"status": "healthy"}


@router.get("/db")
def health_db(db: Session = Depends(get_db)) -> dict[str, str]:
    """Check database connectivity."""
    try:
        # using the session / connection from the dependency
        db.execute(text("SELECT 1"))
        return {"db": "ok"}
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="DB unreachable"
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="DB unreachable"
        )
