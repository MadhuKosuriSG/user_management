"""API v1 package for endpoints."""

# Router is defined in the routes/__init__.py file
from app.api.v1.routes import api_router

__all__ = ["api_router"]
