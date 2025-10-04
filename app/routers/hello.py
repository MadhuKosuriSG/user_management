"""Hello world API endpoint module."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
def read_hello() -> dict[str, str]:
    """Return hello world message."""
    return {"message": "Hello, World! version 1.0"}
