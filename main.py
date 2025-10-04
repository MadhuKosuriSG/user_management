"""Main application module for FastAPI app."""

from fastapi import FastAPI

from app.api import router

app = FastAPI()
app.include_router(router)
