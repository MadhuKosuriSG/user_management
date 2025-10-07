"""API v1 routes package."""

from fastapi import APIRouter

from app.api.v1.routes import books, health

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(books.router, prefix="/books", tags=["books"])
