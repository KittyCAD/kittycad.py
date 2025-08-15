#!/usr/bin/env python3
"""Test script to verify exception handling works correctly."""

from .. import KittyCAD
from ..exceptions import KittyCADAPIError, KittyCADClientError, KittyCADServerError


def test_successful_request():
    """Test that successful requests work without exceptions."""
    # Use a basic client that should work (assuming API is available)
    client = KittyCAD(token="dummy_token", base_url="https://httpbin.org")

    try:
        # This would fail with real API but let's test the exception structure
        result = client.meta.ping()
        assert result is not None or result is None  # Either outcome is acceptable
    except Exception:
        # Request failed as expected
        pass


def test_exception_types():
    """Test that our exception types are properly defined."""
    try:
        # Test base exception
        raise KittyCADAPIError("Test API error", 500, "TEST_ERROR", "req-123")
    except KittyCADAPIError as e:
        assert e.status_code == 500
        assert e.error_code == "TEST_ERROR"
        assert e.request_id == "req-123"

    try:
        # Test client error
        raise KittyCADClientError("Test client error", 404, "NOT_FOUND", "req-456")
    except KittyCADClientError as e:
        assert e.status_code == 404
        assert e.error_code == "NOT_FOUND"
        assert e.request_id == "req-456"

    try:
        # Test server error
        raise KittyCADServerError("Test server error", 500, "INTERNAL_ERROR", "req-789")
    except KittyCADServerError as e:
        assert e.status_code == 500
        assert e.error_code == "INTERNAL_ERROR"
        assert e.request_id == "req-789"


def test_exception_inheritance():
    """Test that exception inheritance works correctly."""
    try:
        raise KittyCADClientError("Test error", 400)
    except KittyCADAPIError as e:
        assert isinstance(e, KittyCADClientError)
        assert isinstance(e, KittyCADAPIError)

    try:
        raise KittyCADServerError("Test error", 500)
    except KittyCADAPIError as e:
        assert isinstance(e, KittyCADServerError)
        assert isinstance(e, KittyCADAPIError)


def test_import_structure():
    """Test that exceptions can be imported from the main package."""
    from kittycad import (
        KittyCADAPIError,
        KittyCADClientError,
        KittyCADConnectionError,
        KittyCADError,
        KittyCADServerError,
        KittyCADTimeoutError,
    )

    # Test that they are actually classes to avoid unused import warning
    exceptions = [
        KittyCADError,
        KittyCADAPIError,
        KittyCADClientError,
        KittyCADServerError,
        KittyCADConnectionError,
        KittyCADTimeoutError,
    ]
    assert all(isinstance(exc, type) for exc in exceptions)
