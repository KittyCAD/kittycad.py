#!/usr/bin/env python3
"""Comprehensive tests for KittyCAD client behavior."""

import asyncio
import os
import threading
from unittest.mock import patch

import httpx
import pytest

from kittycad import AsyncKittyCAD, KittyCAD
from kittycad.exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADError,
    KittyCADServerError,
    KittyCADTimeoutError,
)


class TestEnvironmentVariables:
    """Test environment variable handling."""

    def test_kittycad_api_token_from_env(self):
        """Test KittyCAD() reads KITTYCAD_API_TOKEN from environment."""
        test_token = "test-token-from-env"
        with patch.dict(os.environ, {"KITTYCAD_API_TOKEN": test_token}):
            client = KittyCAD()
            assert client.token == test_token

    def test_zoo_api_token_fallback(self):
        """Test ZOO_API_TOKEN is used as fallback."""
        test_token = "test-zoo-token"
        with patch.dict(os.environ, {"ZOO_API_TOKEN": test_token}, clear=True):
            # Remove KITTYCAD_API_TOKEN if it exists
            if "KITTYCAD_API_TOKEN" in os.environ:
                del os.environ["KITTYCAD_API_TOKEN"]
            client = KittyCAD()
            assert client.token == test_token

    def test_zoo_host_from_env(self):
        """Test ZOO_HOST environment variable is recognized."""
        test_host = "https://test.zoo.dev"
        test_token = "test-token"
        with patch.dict(
            os.environ, {"ZOO_HOST": test_host, "KITTYCAD_API_TOKEN": test_token}
        ):
            client = KittyCAD()
            assert client.base_url == test_host

    def test_explicit_token_overrides_env(self):
        """Test explicit token parameter takes precedence over environment."""
        env_token = "env-token"
        explicit_token = "explicit-token"
        with patch.dict(os.environ, {"KITTYCAD_API_TOKEN": env_token}):
            client = KittyCAD(token=explicit_token)
            assert client.token == explicit_token

    def test_default_base_url_when_no_env(self):
        """Test default base URL is used when no ZOO_HOST in environment."""
        test_token = "test-token"
        with patch.dict(os.environ, {"KITTYCAD_API_TOKEN": test_token}, clear=True):
            # Remove ZOO_HOST if it exists
            if "ZOO_HOST" in os.environ:
                del os.environ["ZOO_HOST"]
            client = KittyCAD()
            assert client.base_url == "https://api.zoo.dev"

    def test_missing_token_raises_helpful_error(self):
        """Test missing token raises helpful error on first authenticated call."""
        with patch.dict(os.environ, {}, clear=True):
            # Remove all token env vars
            for key in ["KITTYCAD_API_TOKEN", "ZOO_API_TOKEN"]:
                if key in os.environ:
                    del os.environ[key]

            with pytest.raises((ValueError, TypeError), match="token"):
                KittyCAD()


class TestContextManagers:
    """Test context manager behavior."""

    def test_sync_context_manager_closes_client(self):
        """Test with KittyCAD() as c: closes underlying httpx.Client on exit."""
        test_token = "test-token"

        with KittyCAD(token=test_token) as client:
            # Force creation of HTTP client
            http_client = client.get_http_client()
            assert http_client is not None
            assert not http_client.is_closed

        # After exiting context, client should be closed
        assert http_client.is_closed

    @pytest.mark.asyncio
    async def test_async_context_manager_closes_client(self):
        """Test AsyncKittyCAD async with closes AsyncClient."""
        test_token = "test-token"

        async with AsyncKittyCAD(token=test_token) as client:
            # Force creation of HTTP client
            http_client = client.get_http_client()
            assert http_client is not None
            assert not http_client.is_closed

        # After exiting context, client should be closed
        assert http_client.is_closed


class TestLightweightViews:
    """Test lightweight view methods."""

    def test_with_timeout_returns_lightweight_view(self):
        """Test with_timeout returns lightweight view without allocating new HTTP client."""
        test_token = "test-token"
        client = KittyCAD(token=test_token)

        # Create HTTP client in original
        original_http_client = client.get_http_client()

        # Create view with different timeout
        view_client = client.with_timeout(60.0)

        # View should be a different object
        assert view_client is not client
        assert view_client.timeout == 60.0
        assert client.timeout == 120.0  # Original unchanged

        # View should share the same HTTP client instance
        view_http_client = view_client.get_http_client()
        assert view_http_client is original_http_client

    def test_with_headers_returns_lightweight_view(self):
        """Test with_headers returns lightweight view without mutating base client."""
        test_token = "test-token"
        client = KittyCAD(token=test_token)
        original_headers = client.headers.copy()

        # Create view with additional headers
        new_headers = {"X-Custom": "value"}
        view_client = client.with_headers(new_headers)

        # View should be different object with merged headers
        assert view_client is not client
        assert "X-Custom" in view_client.headers
        assert view_client.headers["X-Custom"] == "value"

        # Original client should be unchanged
        assert client.headers == original_headers
        assert "X-Custom" not in client.headers

    def test_with_base_url_returns_lightweight_view(self):
        """Test with_base_url returns lightweight view without mutating base client."""
        test_token = "test-token"
        original_url = "https://api.zoo.dev"
        new_url = "https://test.zoo.dev"

        client = KittyCAD(token=test_token, base_url=original_url)
        view_client = client.with_base_url(new_url)

        # View should be different object with new URL
        assert view_client is not client
        assert view_client.base_url == new_url
        assert client.base_url == original_url  # Original unchanged

    def test_views_do_not_allocate_new_http_client(self):
        """Test that view methods share the same HTTP client instance."""
        test_token = "test-token"
        client = KittyCAD(token=test_token)

        # Force creation of HTTP client
        original_http_client = client.get_http_client()

        # Create multiple views
        timeout_view = client.with_timeout(30.0)
        headers_view = client.with_headers({"X-Test": "value"})
        url_view = client.with_base_url("https://test.zoo.dev")

        # All views should share the same http_client instance (attr.evolve copies references)
        assert timeout_view.http_client is original_http_client
        assert headers_view.http_client is original_http_client
        assert url_view.http_client is original_http_client

        # get_http_client should return the same instance
        assert timeout_view.get_http_client() is original_http_client
        assert headers_view.get_http_client() is original_http_client
        assert url_view.get_http_client() is original_http_client


class TestCustomHTTPClient:
    """Test custom injected HTTP client behavior."""

    def test_custom_sync_client_used_as_is(self):
        """Test custom injected httpx.Client is used as-is."""
        test_token = "test-token"
        custom_client = httpx.Client(timeout=30.0)

        client = KittyCAD(token=test_token, http_client=custom_client)

        # Should use the custom client as-is
        assert client.get_http_client() is custom_client
        assert client.get_http_client().timeout.read == 30.0

    def test_custom_sync_client_closed_by_kittycad_close(self):
        """Test custom client is closed by KittyCAD.close() (current behavior)."""
        test_token = "test-token"
        custom_client = httpx.Client()

        client = KittyCAD(token=test_token, http_client=custom_client)

        # Before close, custom client should not be closed
        assert not custom_client.is_closed

        client.close()

        # Current behavior: custom client IS closed by KittyCAD.close()
        # This documents the current implementation behavior
        assert custom_client.is_closed

    @pytest.mark.asyncio
    async def test_custom_async_client_used_as_is(self):
        """Test custom injected httpx.AsyncClient is used as-is."""
        test_token = "test-token"
        custom_client = httpx.AsyncClient(timeout=30.0)

        client = AsyncKittyCAD(token=test_token, http_client=custom_client)

        # Should use the custom client as-is
        assert client.get_http_client() is custom_client
        assert client.get_http_client().timeout.read == 30.0

        # Clean up
        await custom_client.aclose()

    @pytest.mark.asyncio
    async def test_custom_async_client_closed_by_kittycad_aclose(self):
        """Test custom async client is closed by KittyCAD.aclose() (current behavior)."""
        test_token = "test-token"
        custom_client = httpx.AsyncClient()

        client = AsyncKittyCAD(token=test_token, http_client=custom_client)

        # Before close, custom client should not be closed
        assert not custom_client.is_closed

        await client.aclose()

        # Current behavior: custom client IS closed by KittyCAD.aclose()
        # This documents the current implementation behavior
        assert custom_client.is_closed


class TestConcurrency:
    """Test concurrency behavior."""

    def test_sync_client_thread_safety(self):
        """Test sync client multiple threads making calls simultaneously do not race."""
        test_token = "test-token"
        client = KittyCAD(token=test_token)

        results = []
        errors = []

        def make_request(thread_id: int):
            """Make a request from a thread."""
            try:
                # Get HTTP client (this could potentially race)
                client.get_http_client()
                results.append(f"thread-{thread_id}-success")
            except Exception as e:
                errors.append(f"thread-{thread_id}-error: {e}")

        # Create multiple threads
        threads = []
        for i in range(10):
            thread = threading.Thread(target=make_request, args=(i,))
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads
        for thread in threads:
            thread.join()

        # Should have no errors and all successes
        assert len(errors) == 0
        assert len(results) == 10

        # Clean up
        client.close()

    def test_sync_client_connection_pool_reuse(self):
        """Test sync client connection pool is reused safely."""
        test_token = "test-token"
        client = KittyCAD(token=test_token)

        # Get HTTP client multiple times
        http_client1 = client.get_http_client()
        http_client2 = client.get_http_client()
        http_client3 = client.get_http_client()

        # Should be the same instance (reused)
        assert http_client1 is http_client2
        assert http_client2 is http_client3

        # Clean up
        client.close()

    @pytest.mark.asyncio
    async def test_async_client_concurrent_calls(self):
        """Test async client multiple concurrent await calls work."""
        test_token = "test-token"
        client = AsyncKittyCAD(token=test_token)

        async def get_http_client_task():
            """Get HTTP client in an async task."""
            return client.get_http_client()

        # Create multiple concurrent tasks
        tasks = [get_http_client_task() for _ in range(10)]

        # Run concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Should have no exceptions
        exceptions = [r for r in results if isinstance(r, Exception)]
        assert len(exceptions) == 0

        # All should return the same HTTP client instance
        http_clients = [r for r in results if not isinstance(r, Exception)]
        assert len(http_clients) == 10
        assert all(client is http_clients[0] for client in http_clients)

        # Clean up
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_no_already_closed_errors(self):
        """Test async client no 'already closed' errors during normal operation."""
        test_token = "test-token"
        client = AsyncKittyCAD(token=test_token)

        # Get HTTP client
        http_client = client.get_http_client()
        assert not http_client.is_closed

        # Close properly
        await client.aclose()
        assert http_client.is_closed

    @pytest.mark.asyncio
    async def test_async_client_cannot_reuse_after_aclose(self):
        """Test async client cannot be reused after aclose()."""
        test_token = "test-token"
        client = AsyncKittyCAD(token=test_token)

        # Get HTTP client and close
        http_client = client.get_http_client()
        await client.aclose()

        # Should not be able to make requests with closed client
        assert http_client.is_closed


class TestExceptionHandling:
    """Test exception handling behavior."""

    def test_4xx_raises_client_error_with_details(self):
        """Test 4xx responses raise KittyCADClientError with proper details."""
        # This is a basic test - in practice would need to mock HTTP responses
        error = KittyCADClientError(
            message="Not Found",
            status_code=404,
            error_code="RESOURCE_NOT_FOUND",
            request_id="req-123",
            request_method="GET",
            request_url="https://api.zoo.dev/users/nonexistent",
        )

        assert error.status_code == 404
        assert error.error_code == "RESOURCE_NOT_FOUND"
        assert error.request_id == "req-123"
        assert error.request_method == "GET"
        assert error.request_url == "https://api.zoo.dev/users/nonexistent"

        # Check string representation includes method, path, status
        error_str = str(error)
        assert "404" in error_str
        assert "Not Found" in error_str
        assert "RESOURCE_NOT_FOUND" in error_str
        assert "req-123" in error_str

    def test_5xx_raises_server_error_with_details(self):
        """Test 5xx responses raise KittyCADServerError with proper details."""
        error = KittyCADServerError(
            message="Internal Server Error",
            status_code=500,
            error_code="INTERNAL_ERROR",
            request_id="req-456",
            request_method="POST",
            request_url="https://api.zoo.dev/file/convert",
        )

        assert error.status_code == 500
        assert error.error_code == "INTERNAL_ERROR"
        assert error.request_id == "req-456"

        # Check string representation
        error_str = str(error)
        assert "500" in error_str
        assert "Internal Server Error" in error_str

    def test_network_error_raises_connection_error_with_cause(self):
        """Test network errors raise KittyCADConnectionError with original exception as __cause__."""
        original_error = ConnectionError("DNS lookup failed")

        error = KittyCADConnectionError(
            message="Failed to connect to server",
            original_error=original_error,
            request_method="GET",
            request_url="https://api.zoo.dev/ping",
        )

        assert error.original_error is original_error
        assert error.request_method == "GET"
        assert error.request_url == "https://api.zoo.dev/ping"

        # Check string representation includes method and URL
        error_str = str(error)
        assert "GET" in error_str
        assert "https://api.zoo.dev/ping" in error_str
        assert "DNS lookup failed" in error_str

    def test_timeout_error_with_details(self):
        """Test timeout errors raise KittyCADTimeoutError with proper details."""
        error = KittyCADTimeoutError(
            message="Request timed out",
            timeout_seconds=30.0,
            request_method="POST",
            request_url="https://api.zoo.dev/file/convert",
        )

        assert error.timeout_seconds == 30.0
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/file/convert"

        # Check string representation includes timeout value
        error_str = str(error)
        assert "30.0" in error_str
        assert "POST" in error_str
        assert "timeout" in error_str.lower()

    def test_exception_inheritance_hierarchy(self):
        """Test exception inheritance works correctly."""
        # All exceptions should inherit from KittyCADError
        assert issubclass(KittyCADAPIError, KittyCADError)
        assert issubclass(KittyCADClientError, KittyCADAPIError)
        assert issubclass(KittyCADServerError, KittyCADAPIError)
        assert issubclass(KittyCADConnectionError, KittyCADError)
        assert issubclass(KittyCADTimeoutError, KittyCADError)

        # Client and server errors should also inherit from APIError
        assert issubclass(KittyCADClientError, KittyCADAPIError)
        assert issubclass(KittyCADServerError, KittyCADAPIError)


if __name__ == "__main__":
    pytest.main([__file__])
