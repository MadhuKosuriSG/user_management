"""Books api routes module."""

from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_books() -> list[dict[str, str]]:
    """List all books."""
    return [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"},
    ]


@router.get("/{book_id}")
def get_book(book_id: int) -> Any:
    """Get book details by ID."""
    books = {1: {"title": "1984", "author": "George Orwell", "year": 1949}}
    return books.get(book_id, {"error": "Book not found"})
