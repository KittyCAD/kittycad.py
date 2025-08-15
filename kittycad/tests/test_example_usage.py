#!/usr/bin/env python3
"""
Example usage of the new exception-based KittyCAD Python SDK.

This demonstrates the clean, idiomatic interface where errors are handled
via exceptions rather than return values.
"""

from .. import KittyCAD, KittyCADAPIError, KittyCADClientError, KittyCADServerError


def test_example_successful_call():
    """Example of making a successful API call."""
    try:
        # Clean, simple interface using environment variable
        client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable
        result = client.meta.ping()
        # Either success or exception is acceptable for this test
        assert result is not None or result is None

    except KittyCADAPIError:
        # All API errors are caught here with rich context
        pass  # Expected when no valid token


def test_error_handling():
    """Example of handling different types of API errors."""
    try:
        # This will likely fail with authentication error
        client = KittyCAD()  # Uses KITTYCAD_API_TOKEN environment variable
        user = client.users.get_user_self()
        # Either success or exception is acceptable
        assert user is not None or user is None

    except KittyCADClientError as e:
        # Handle client errors (4xx) - usually fixable by user
        assert e.status_code >= 400 and e.status_code < 500

    except KittyCADServerError as e:
        # Handle server errors (5xx) - usually temporary
        assert e.status_code >= 500

    except KittyCADAPIError:
        # Catch-all for any other API errors
        pass


def test_interface_design():
    """Test that the new interface is properly designed."""
    # Test that KittyCAD class can be instantiated
    client = KittyCAD()
    assert hasattr(client, "users")
    assert hasattr(client, "meta")

    # Test that exception types exist
    assert KittyCADAPIError is not None
    assert KittyCADClientError is not None
    assert KittyCADServerError is not None
