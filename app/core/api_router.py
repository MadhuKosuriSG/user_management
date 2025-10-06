"""Core API router module for FastAPI application."""

from fastapi import APIRouter

from app.api.v1.routes import api_router as api_v1_router

# Main API Router
router = APIRouter()

# Include versioned API routers
router.include_router(api_v1_router, prefix="/api/v1")
