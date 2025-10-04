# FastAPI Production-Ready Project

This is a scalable and maintainable FastAPI project with a proper structure for production use.

## Project Structure

```
.
├── app/                    # Application package
│   ├── core/               # Core modules (config, security, etc.)
│   ├── models/             # SQLAlchemy models or other DB models
│   ├── routers/            # API route definitions
│   ├── schemas/            # Pydantic schemas for request/response models
│   ├── services/           # Business logic
│   └── api.py              # Main API router
├── tests/                  # Test directory
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── conftest.py         # Test fixtures and configuration
├── .github/                # GitHub specific files
│   └── workflows/          # CI/CD workflows
├── .vscode/                # VS Code settings
├── .env                    # Environment variables (not tracked by git)
├── .gitignore              # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── main.py                 # Application entry point
├── pyproject.toml          # Tool configuration
├── requirements.txt        # Project dependencies
└── setup.cfg               # Pytest configuration
```

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Install pre-commit hooks:
   ```
   pre-commit install
   ```

## Running the Application

```bash
uvicorn main:app --reload
```

API will be available at http://127.0.0.1:8000

## Running Tests

```bash
pytest
```

For test coverage report:

```bash
pytest --cov=app
```

## Code Style and Quality

This project uses:
- Black for code formatting
- isort for import sorting
- Flake8 for linting
- MyPy for static type checking
- Pre-commit hooks to enforce these on commits

## VS Code Extensions

Recommended extensions:
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Black Formatter (ms-python.black-formatter)
- isort (ms-python.isort)
- Even Better TOML (tamasfe.even-better-toml)
- YAML (redhat.vscode-yaml)
- markdownlint (DavidAnson.vscode-markdownlint)
- GitLens (eamodio.gitlens)

## Best Practices for Scalability

1. **Keep Modules Small**: Each module should have a single responsibility
2. **Use Dependency Injection**: Makes testing and extending functionality easier
3. **Consistent Error Handling**: Use FastAPI's HTTPException with proper status codes
4. **Documentation**: Keep docstrings updated
5. **Type Hints**: Always use type annotations
6. **Layered Architecture**: Separate API routes, business logic, and data access
7. **Comprehensive Testing**: Unit test for each component, integration tests for API endpoints
8. **Configuration Management**: Use environment variables for configuration
