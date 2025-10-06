"""Main application module for FastAPI app."""

from fastapi import FastAPI

# Import router from core module instead of api
from app.core.api_router import router

app = FastAPI()
app.include_router(router)
