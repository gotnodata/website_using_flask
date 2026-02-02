# Testing Guide

This Flask application now includes comprehensive testing using pytest.

## Setup

1. Install the testing dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with coverage:
```bash
pytest --cov=. --cov-report=html
```

### Run specific test files:
```bash
pytest tests/test_main.py
pytest tests/test_auth.py
pytest tests/test_models.py
```

### Run with verbose output:
```bash
pytest -v
```

## Test Structure

- `tests/conftest.py` - Contains pytest fixtures for test setup
- `tests/test_main.py` - Tests for main blueprint routes
- `tests/test_auth.py` - Tests for authentication routes
- `tests/test_models.py` - Tests for database models
- `test_config.py` - Test configuration with in-memory database
- `pytest.ini` - Pytest configuration file

## Test Coverage

The tests cover:
- Route responses and status codes
- Database operations
- Session management
- Form submissions
- User authentication flow
- Template rendering

## Configuration

Tests use an in-memory SQLite database for isolation and speed. The test configuration is in `test_config.py`.
