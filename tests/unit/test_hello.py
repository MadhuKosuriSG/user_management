"""Unit tests for the hello API."""

from fastapi.testclient import TestClient


def test_read_hello(client: TestClient) -> None:
    """Test the hello endpoint."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World! version 1.0"}
