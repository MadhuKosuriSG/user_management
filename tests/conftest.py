"""Test fixtures for pytest."""

import pytest
from fastapi.testclient import TestClient

# Local application imports - these imports will work
# once the package is installed in development mode
from main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the app."""
    return TestClient(app)
