"""Books api routes module."""

from typing import List

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.book import BookCreate, BookRead, BookUpdate
from app.services.book_service import BookService

router = APIRouter()


@router.get("/", response_model=List[BookRead])
def list_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
) -> List[BookRead]:
    """
    Get list of books

    Args:
        skip(int): Limit of the values

    Retuns:
        List[BookRead]: List of books
    """
    svc = BookService(db)
    return svc.list_books(skip=skip, limit=limit)


@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)) -> BookRead:
    """
    Get a book by its ID.

    Args:
        book_id (int): The ID of the book to be retrieved.

    Returns:
        BookRead: The retrieved book.
    """
    svc = BookService(db)
    book = svc.get_book(book_id)
    return book


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate, db: Session = Depends(get_db)) -> BookRead:
    """
    Create a new book.

    Args:
        book_in (BookCreate): The book to be created.

    Returns:
        BookRead: The created book.
    """
    svc = BookService(db)
    book = svc.create_book(book_in)
    return book


@router.put("/{book_id}", response_model=BookRead)
def update_book(
    book_id: int, book_in: BookUpdate, db: Session = Depends(get_db)
) -> BookRead:
    """
    Update an existing book.

    Args:
        book_id (int): The ID of the book to be updated.
        book_in (BookUpdate): The updated book data.

    Returns:
        BookRead: The updated book.
    """
    svc = BookService(db)
    book = svc.update_book(book_id, book_in)
    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)) -> None:
    """
    Delete a book by its ID.

    Args:
        book_id (int): The ID of the book to be deleted.
    """
    svc = BookService(db)
    return svc.delete_book(book_id)
