"""Books api routes module."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_books() -> list[dict[str, str]]:
    """List all books."""
    return [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"},
    ]
