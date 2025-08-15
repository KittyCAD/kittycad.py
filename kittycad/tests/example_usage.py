#!/usr/bin/env python3
"""
Example usage of the new exception-based KittyCAD Python SDK.

This demonstrates the clean, idiomatic interface where errors are handled
via exceptions rather than return values.
"""

import os

from .. import KittyCADAPIError, KittyCADClientError, KittyCADServerError
from ..api.meta import ping
from ..api.users import get_user_self
from ..client import ClientFromEnv


def example_successful_call():
    """Example of making a successful API call."""
    print("=== Example: Successful API Call ===")

    try:
        client = ClientFromEnv()

        # Clean, simple interface - no need to check for error types
        result = ping.sync(client=client)
        print(f"✓ Ping successful: {result}")

    except KittyCADAPIError as e:
        # All API errors are caught here with rich context
        print(f"✗ API call failed: {e}")
        print(f"  Status code: {e.status_code}")
        print(f"  Error code: {e.error_code}")
        print(f"  Request ID: {e.request_id}")


def example_error_handling():
    """Example of handling different types of API errors."""
    print("\n=== Example: Error Handling ===")

    try:
        # This will likely fail with authentication error
        client = ClientFromEnv()
        user = get_user_self.sync(client=client)
        print(f"✓ User info: {user}")

    except KittyCADClientError as e:
        # Handle client errors (4xx) - usually fixable by user
        print(f"✗ Client error: {e}")
        if e.status_code == 401:
            print("  → Check your API token")
        elif e.status_code == 403:
            print("  → You don't have permission for this operation")
        elif e.status_code == 404:
            print("  → Resource not found")

    except KittyCADServerError as e:
        # Handle server errors (5xx) - usually temporary
        print(f"✗ Server error: {e}")
        print("  → This is likely temporary, try again later")

    except KittyCADAPIError as e:
        # Catch-all for any other API errors
        print(f"✗ API error: {e}")


def example_old_vs_new():
    """Compare old vs new interface."""
    print("\n=== Old vs New Interface Comparison ===")

    print("OLD (error-prone):")
    print("""
    result = kittycad.api.users.get_user_self(client=client)
    if isinstance(result, Error):
        print(f"Error: {result.message}")
        return
    
    # User has to remember to check for errors every time
    user = result  # This could be None or Error!
    """)

    print("NEW (clean & idiomatic):")
    print("""
    try:
        user = kittycad.api.users.get_user_self(client=client)
        # user is guaranteed to be the expected type or an exception was raised
        
    except KittyCADAPIError as e:
        print(f"Call failed: {e}")
        # Rich error context including status code, error code, request ID, URL
    """)


def main():
    """Run example usage."""
    print("KittyCAD Python SDK - Exception-Based Interface\n")

    # Check if API token is available
    if not os.getenv("KITTYCAD_API_TOKEN") and not os.getenv("ZOO_API_TOKEN"):
        print(
            "⚠️  No API token found. Set KITTYCAD_API_TOKEN or ZOO_API_TOKEN to run live examples."
        )
        print(
            "    The examples below will show the exception interface even with failures.\n"
        )

    example_old_vs_new()

    # These will work with or without tokens to demonstrate the interface
    example_successful_call()
    example_error_handling()

    print(
        "\n✓ Examples completed. The SDK now provides clean exception-based error handling!"
    )


if __name__ == "__main__":
    main()
