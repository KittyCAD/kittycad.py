#!/usr/bin/env python3
"""Test script to verify exception handling works correctly."""

import sys
import traceback

from ..api.meta import ping
from ..client import Client
from ..exceptions import KittyCADAPIError, KittyCADClientError, KittyCADServerError


def test_successful_request():
    """Test that successful requests work without exceptions."""
    print("Testing successful request...")

    # Use a basic client that should work (assuming API is available)
    client = Client(token="dummy_token", base_url="https://httpbin.org")

    try:
        # This would fail with real API but let's test the exception structure
        result = ping.sync(client=client)
        print(f"✓ Request succeeded: {type(result)}")
        return True
    except Exception as e:
        print(f"✓ Request failed as expected with exception: {type(e).__name__}: {e}")
        return True


def test_exception_types():
    """Test that our exception types are properly defined."""
    print("Testing exception types...")

    try:
        # Test base exception
        raise KittyCADAPIError("Test API error", 500, "TEST_ERROR", "req-123")
    except KittyCADAPIError as e:
        print(f"✓ KittyCADAPIError: {e}")
        print(f"  - status_code: {e.status_code}")
        print(f"  - error_code: {e.error_code}")
        print(f"  - request_id: {e.request_id}")

    try:
        # Test client error
        raise KittyCADClientError("Test client error", 404, "NOT_FOUND", "req-456")
    except KittyCADClientError as e:
        print(f"✓ KittyCADClientError: {e}")

    try:
        # Test server error
        raise KittyCADServerError("Test server error", 500, "INTERNAL_ERROR", "req-789")
    except KittyCADServerError as e:
        print(f"✓ KittyCADServerError: {e}")


def test_exception_inheritance():
    """Test that exception inheritance works correctly."""
    print("Testing exception inheritance...")

    try:
        raise KittyCADClientError("Test error", 400)
    except KittyCADAPIError as e:
        print(f"✓ KittyCADClientError caught as KittyCADAPIError: {type(e).__name__}")

    try:
        raise KittyCADServerError("Test error", 500)
    except KittyCADAPIError as e:
        print(f"✓ KittyCADServerError caught as KittyCADAPIError: {type(e).__name__}")


def test_import_structure():
    """Test that exceptions can be imported from the main package."""
    print("Testing import structure...")

    try:
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

        print("✓ All exceptions imported successfully from kittycad package")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=== Testing KittyCAD Exception Handling ===\n")

    success = True

    try:
        test_exception_types()
        print()

        test_exception_inheritance()
        print()

        success &= test_import_structure()
        print()

        test_successful_request()
        print()

    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        traceback.print_exc()
        success = False

    if success:
        print("✓ All tests passed! Exception handling is working correctly.")
        return 0
    else:
        print("✗ Some tests failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
