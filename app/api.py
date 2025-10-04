"""API router module for FastAPI application."""

from fastapi import APIRouter

from app.routers import health, hello

# Main API Router
router = APIRouter()

# Include modular routers
router.include_router(health.router, tags=["health"])
router.include_router(hello.router, tags=["hello"])
