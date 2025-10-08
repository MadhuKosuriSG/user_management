from fastapi import HTTPException, status
from sqlalchemy.orm import Session as DBSession

from app.models.book import Book
from app.repositories.book_repo import BookRepository
from app.schemas.book import BookCreate, BookUpdate


class BookService:
    def __init__(self, db: DBSession):
        self.db: DBSession = db
        self.repo = BookRepository(db)

    def create_book(self, obj_in: BookCreate) -> Book:
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
        try:
            book = self.repo.create(obj_in)
            self.db.commit()
            self.db.refresh(book)

            if not book:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Failed to create the book",
                )
            return book
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}",
            )

    def get_book(self, book_id: int) -> Book:
        """
        Retrieve a book by its ID.

        Args:
            book_id (int): The ID of the book to be retrieved.

        Returns:
            Book: The retrieved book.

        Raises:
            HTTPException: If the book is not found.
            HTTPException: If an internal server error occurs.
        """
        print(book_id)
        print("In the service method get_book")
        try:
            book = self.repo.get(book_id)
            print(book)
            if not book:
                print("Book not found")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Book not found",
                )
            return book
        except Exception as e:
            print(str(e))
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}",
            )

    def list_books(self, skip: int = 0, limit: int = 100) -> list[Book]:
        """
        List all books.

        Args:
            skip (int, optional): The number of books to skip. Defaults to 0.
            limit (int, optional): The maximum number of books to return. Defaults to 100.

        Returns:
            list[Book]: List of books
        """
        try:
            return self.repo.list(skip=skip, limit=limit)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}",
            )

    def update_book(self, book_id: int, book_in: BookUpdate) -> Book:
        """
        Update an existing book.

        Args:
            book_id (int): The ID of the book to be updated.
            book_in (BookUpdate): The updated book data.

        Returns:
            Book: The updated book.

        Raises:
            HTTPException: If the book is not found.
            HTTPException: If an internal server error occurs.
        """
        try:
            book = self.repo.get(book_id)
            if not book:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Book not found",
                )
            self.repo.update(book, book_in)
            self.db.commit()
            self.db.refresh(book)
            return book
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}",
            )

    def delete_book(self, book_id: int) -> None:
        """
        Delete a book by its ID.

        Args:
            book_id (int): The ID of the book to be deleted.

        Raises:
            HTTPException: If the book is not found.
            HTTPException: If an internal server error occurs.
        """
        try:
            book = self.repo.get(book_id)
            if not book:
                print("Book not found")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Book not found",
                )
            self.repo.delete(book)
            self.db.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}",
            )
