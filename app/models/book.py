"""Implement the database model for books."""

from sqlalchemy import Column, Float, Integer, String, Text

from app.db.session import Base


class Book(Base):
    """Define the Book database model."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    def __repr__(self) -> str:
        """Return string representation of Book."""
        return f"<Book {self.title} by {self.author}>"
