from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


class BookRepository:
    def __init__(self, db: Session):
        """
        Initialize the BookRepository.

        Args:
            db (Session): The SQLAlchemy session.
        """
        self.db = db

    def get(self, book_id: int) -> Optional[Book]:
        """
        Retrieve a book by its ID.

        Args:
            book_id (int): The ID of the book to be retrieved.

        Returns:
            Optional[Book]: The retrieved book, or None if not found.
        """
        print(book_id)
        print(type(book_id))
        stmt = select(Book).where(Book.id == book_id)
        print(stmt)
        result = self.db.scalars(stmt).first()
        return result

    def list(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """
        List all books.

        Args:
            skip (int, optional): The number of books to skip. Defaults to 0.
            limit (int, optional): The maximum number of books to return. Defaults to 100.

        Returns:
            List[Book]: List of books
        """
        result = self.db.query(Book).offset(skip).limit(limit).all()
        return result

    def create(self, obj_in: BookCreate) -> Book:
        """
        Create a new book.

        Args:
            obj_in (BookCreate): The book data to be created.

        Returns:
            Book: The created book.

        Raises:
            HTTPException: If the book creation fails.
            HTTPException: If an internal server error occurs.
        """
        db_obj = Book(**obj_in.dict())
        self.db.add(db_obj)
        self.db.flush()
        return db_obj

    def update(self, db_obj: Book, obj_in: BookUpdate) -> Book:
        """
        Update an existing book.

        Args:
            db_obj (Book): The book to be updated.
            obj_in (BookUpdate): The updated book data.

        Returns:
            Book: The updated book.

        Raises:
            HTTPException: If the book update fails.
            HTTPException: If an internal server error occurs.
        """
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        self.db.add(db_obj)
        return db_obj

    def delete(self, db_obj: Book) -> None:
        """
        Delete a book.

        Args:
            db_obj (Book): The book to be deleted.
        """
        self.db.delete(db_obj)
