"""Database session and connection management module."""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.core.config import settings

# create_engine for MySQL (pymysql). pool options are tuned for dev.
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # validate connections are alive
    pool_size=5,  # small pool for dev
    max_overflow=10,  # allow some bursts
    pool_recycle=1800,  # recycle connections after 30min
    echo=False,  # set True if you want SQL echo for debugging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """Provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
