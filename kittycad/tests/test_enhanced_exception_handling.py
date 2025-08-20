#!/usr/bin/env python3
"""Comprehensive tests for enhanced exception handling in KittyCAD SDK."""

from unittest.mock import Mock, patch

import httpx
import pytest

from kittycad.exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADError,
    KittyCADServerError,
    KittyCADTimeoutError,
)
from kittycad.response_helpers import (
    make_async_request_with_error_handling,
    make_request_with_error_handling,
    raise_for_status,
    wrap_httpx_exceptions,
)


class TestEnhancedExceptionTypes:
    """Test enhanced exception types with additional attributes."""

    def test_kittycad_error_basic(self):
        """Test basic KittyCADError functionality."""
        error = KittyCADError("Test error")
        assert error.message == "Test error"
        assert error.request_id is None
        assert str(error) == "Test error"

    def test_kittycad_error_with_request_id(self):
        """Test KittyCADError with request ID."""
        error = KittyCADError("Test error", request_id="req-123")
        assert error.message == "Test error"
        assert error.request_id == "req-123"
        assert str(error) == "Test error (request_id: req-123)"

    def test_kittycad_api_error_enhanced_attributes(self):
        """Test KittyCADAPIError with enhanced attributes."""
        error = KittyCADAPIError(
            message="API error",
            status_code=400,
            error_code="INVALID_PARAM",
            request_id="req-456",
            headers={"x-custom": "value"},
            request_method="POST",
            request_url="https://api.zoo.dev/test",
        )

        assert error.message == "API error"
        assert error.status_code == 400
        assert error.error_code == "INVALID_PARAM"
        assert error.request_id == "req-456"
        assert error.headers == {"x-custom": "value"}
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/test"
        assert (
            str(error)
            == "HTTP 400: API error (error_code: INVALID_PARAM) (request_id: req-456)"
        )

    def test_kittycad_connection_error_enhanced(self):
        """Test KittyCADConnectionError with enhanced attributes."""
        original_error = ConnectionError("DNS resolution failed")
        error = KittyCADConnectionError(
            message="Connection failed",
            original_error=original_error,
            request_method="GET",
            request_url="https://api.zoo.dev/test",
        )

        assert error.message == "Connection failed"
        assert error.original_error == original_error
        assert error.request_method == "GET"
        assert error.request_url == "https://api.zoo.dev/test"
        assert "Connection failed (request to GET https://api.zoo.dev/test)" in str(
            error
        )
        assert "[caused by: DNS resolution failed]" in str(error)

    def test_kittycad_timeout_error_enhanced(self):
        """Test KittyCADTimeoutError with enhanced attributes."""
        error = KittyCADTimeoutError(
            message="Request timed out",
            timeout_seconds=30.0,
            request_method="POST",
            request_url="https://api.zoo.dev/slow",
        )

        assert error.message == "Request timed out"
        assert error.timeout_seconds == 30.0
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/slow"
        assert (
            "Request timed out (timeout: 30.0s) (request to POST https://api.zoo.dev/slow)"
            == str(error)
        )


class TestHTTPXExceptionWrapping:
    """Test wrapping of HTTPX exceptions into KittyCAD exceptions."""

    def test_wrap_httpx_timeout_exception(self):
        """Test wrapping of HTTPX TimeoutException."""

        @wrap_httpx_exceptions(
            request_method="GET", request_url="https://api.zoo.dev/test"
        )
        def timeout_function():
            raise httpx.TimeoutException("Read timeout")

        with pytest.raises(KittyCADTimeoutError) as exc_info:
            timeout_function()

        error = exc_info.value
        assert "Request timed out: Read timeout" in error.message
        assert error.request_method == "GET"
        assert error.request_url == "https://api.zoo.dev/test"
        assert isinstance(error.__cause__, httpx.TimeoutException)

    def test_wrap_httpx_connect_error(self):
        """Test wrapping of HTTPX ConnectError."""

        @wrap_httpx_exceptions(
            request_method="POST", request_url="https://api.zoo.dev/test"
        )
        def connect_error_function():
            raise httpx.ConnectError("Connection refused")

        with pytest.raises(KittyCADConnectionError) as exc_info:
            connect_error_function()

        error = exc_info.value
        assert "Connection failed: Connection refused" in error.message
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/test"
        assert isinstance(error.original_error, httpx.ConnectError)
        assert isinstance(error.__cause__, httpx.ConnectError)

    def test_wrap_httpx_network_error(self):
        """Test wrapping of generic HTTPX NetworkError."""

        @wrap_httpx_exceptions(
            request_method="PUT", request_url="https://api.zoo.dev/test"
        )
        def network_error_function():
            raise httpx.NetworkError("Network unreachable")

        with pytest.raises(KittyCADConnectionError) as exc_info:
            network_error_function()

        error = exc_info.value
        assert "Network error: Network unreachable" in error.message
        assert error.request_method == "PUT"
        assert error.request_url == "https://api.zoo.dev/test"
        assert isinstance(error.original_error, httpx.NetworkError)

    def test_wrap_generic_httpx_request_error(self):
        """Test wrapping of generic HTTPX RequestError."""

        @wrap_httpx_exceptions(
            request_method="DELETE", request_url="https://api.zoo.dev/test"
        )
        def request_error_function():
            raise httpx.RequestError("Generic request error")

        with pytest.raises(KittyCADConnectionError) as exc_info:
            request_error_function()

        error = exc_info.value
        assert "Request error: Generic request error" in error.message
        assert error.request_method == "DELETE"
        assert error.request_url == "https://api.zoo.dev/test"
        assert isinstance(error.original_error, httpx.RequestError)


class TestEnhancedRaiseForStatus:
    """Test the enhanced raise_for_status function."""

    def test_raise_for_status_with_enhanced_context(self):
        """Test that raise_for_status includes enhanced context."""
        # Mock response with request context
        response = Mock(spec=httpx.Response)
        response.is_success = False
        response.status_code = 404
        response.reason_phrase = "Not Found"
        response.headers = {
            "x-request-id": "req-789",
            "content-type": "application/json",
        }
        response.url = "https://api.zoo.dev/users/nonexistent"
        response.json.return_value = {
            "message": "User not found",
            "error_code": "USER_NOT_FOUND",
            "request_id": "req-789",
        }

        # Mock request
        mock_request = Mock()
        mock_request.method = "GET"
        response.request = mock_request

        with pytest.raises(KittyCADClientError) as exc_info:
            raise_for_status(response)

        error = exc_info.value
        assert error.status_code == 404
        assert error.error_code == "USER_NOT_FOUND"
        assert error.request_id == "req-789"
        assert error.request_method == "GET"
        assert error.request_url == "https://api.zoo.dev/users/nonexistent"
        assert "404 Not Found: User not found" in error.message

    def test_raise_for_status_server_error_with_context(self):
        """Test raise_for_status for server errors with context."""
        response = Mock(spec=httpx.Response)
        response.is_success = False
        response.status_code = 500
        response.reason_phrase = "Internal Server Error"
        response.headers = {
            "x-request-id": "req-500",
            "content-type": "application/json",
        }
        response.url = "https://api.zoo.dev/internal"
        response.json.return_value = {
            "message": "Database connection failed",
            "error_code": "DB_ERROR",
        }

        mock_request = Mock()
        mock_request.method = "POST"
        response.request = mock_request

        with pytest.raises(KittyCADServerError) as exc_info:
            raise_for_status(response)

        error = exc_info.value
        assert error.status_code == 500
        assert error.error_code == "DB_ERROR"
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/internal"
        # Check that request_id from headers is extracted
        assert error.request_id == "req-500"


class TestRequestHelpersWithErrorHandling:
    """Test the enhanced request helper functions."""

    @patch("httpx.Client")
    def test_make_request_with_error_handling_success(self, mock_client_class):
        """Test successful request using make_request_with_error_handling."""
        # Setup mock client
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Setup mock response
        mock_response = Mock(spec=httpx.Response)
        mock_response.is_success = True
        mock_response.status_code = 200
        mock_client.get.return_value = mock_response

        # Test the function
        response = make_request_with_error_handling(
            mock_client, "get", "https://api.zoo.dev/test"
        )

        assert response == mock_response
        mock_client.get.assert_called_once_with("https://api.zoo.dev/test")

    @patch("httpx.Client")
    def test_make_request_with_error_handling_timeout(self, mock_client_class):
        """Test timeout handling in make_request_with_error_handling."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Make client.get raise TimeoutException
        mock_client.get.side_effect = httpx.TimeoutException("Connection timeout")

        with pytest.raises(KittyCADTimeoutError) as exc_info:
            make_request_with_error_handling(
                mock_client, "get", "https://api.zoo.dev/slow"
            )

        error = exc_info.value
        assert "Request timed out" in error.message
        assert error.request_method == "GET"
        assert error.request_url == "https://api.zoo.dev/slow"

    @patch("httpx.Client")
    def test_make_request_with_error_handling_connection_error(self, mock_client_class):
        """Test connection error handling in make_request_with_error_handling."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Make client.post raise ConnectError
        mock_client.post.side_effect = httpx.ConnectError("Connection refused")

        with pytest.raises(KittyCADConnectionError) as exc_info:
            make_request_with_error_handling(
                mock_client,
                "post",
                "https://api.zoo.dev/offline",
                json={"test": "data"},
            )

        error = exc_info.value
        assert "Connection failed" in error.message
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/offline"


class TestAsyncRequestHelpersWithErrorHandling:
    """Test the enhanced async request helper functions."""

    @pytest.mark.asyncio
    @patch("httpx.AsyncClient")
    async def test_make_async_request_with_error_handling_success(
        self, mock_client_class
    ):
        """Test successful async request using make_async_request_with_error_handling."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Setup mock response
        mock_response = Mock(spec=httpx.Response)
        mock_response.is_success = True
        mock_response.status_code = 200

        # Make the async method return a mock response
        async def mock_get(*args, **kwargs):
            return mock_response

        mock_client.get = mock_get

        response = await make_async_request_with_error_handling(
            mock_client, "get", "https://api.zoo.dev/test"
        )

        assert response == mock_response

    @pytest.mark.asyncio
    @patch("httpx.AsyncClient")
    async def test_make_async_request_with_error_handling_timeout(
        self, mock_client_class
    ):
        """Test timeout handling in make_async_request_with_error_handling."""
        mock_client = Mock()
        mock_client_class.return_value = mock_client

        # Make async method raise TimeoutException
        async def mock_post(*args, **kwargs):
            raise httpx.TimeoutException("Read timeout")

        mock_client.post = mock_post

        with pytest.raises(KittyCADTimeoutError) as exc_info:
            await make_async_request_with_error_handling(
                mock_client, "post", "https://api.zoo.dev/slow"
            )

        error = exc_info.value
        assert "Request timed out" in error.message
        assert error.request_method == "POST"
        assert error.request_url == "https://api.zoo.dev/slow"


class TestExceptionInheritance:
    """Test that exception inheritance is correct for proper exception handling."""

    def test_exception_hierarchy(self):
        """Test that all exceptions inherit from appropriate base classes."""
        # All KittyCAD exceptions should inherit from KittyCADError
        assert issubclass(KittyCADAPIError, KittyCADError)
        assert issubclass(KittyCADClientError, KittyCADError)
        assert issubclass(KittyCADServerError, KittyCADError)
        assert issubclass(KittyCADConnectionError, KittyCADError)
        assert issubclass(KittyCADTimeoutError, KittyCADError)

        # API errors should have the right hierarchy
        assert issubclass(KittyCADClientError, KittyCADAPIError)
        assert issubclass(KittyCADServerError, KittyCADAPIError)

        # All should inherit from standard Exception
        assert issubclass(KittyCADError, Exception)

    def test_catch_base_exception(self):
        """Test that catching KittyCADError catches all KittyCAD exceptions."""
        errors = [
            KittyCADAPIError("API error", 400),
            KittyCADClientError("Client error", 404),
            KittyCADServerError("Server error", 500),
            KittyCADConnectionError("Connection error"),
            KittyCADTimeoutError("Timeout error"),
        ]

        for error in errors:
            try:
                raise error
            except KittyCADError:
                # Should catch all KittyCAD errors
                pass
            except Exception:
                pytest.fail(f"Failed to catch {type(error).__name__} as KittyCADError")

    def test_catch_api_errors(self):
        """Test that catching KittyCADAPIError catches HTTP-related errors."""
        api_errors = [
            KittyCADAPIError("Generic API error", 418),
            KittyCADClientError("Client error", 400),
            KittyCADServerError("Server error", 500),
        ]

        for error in api_errors:
            try:
                raise error
            except KittyCADAPIError:
                # Should catch all API errors
                pass
            except Exception:
                pytest.fail(
                    f"Failed to catch {type(error).__name__} as KittyCADAPIError"
                )

        # Non-API errors should not be caught
        non_api_errors: list[KittyCADError] = [
            KittyCADConnectionError("Connection error"),
            KittyCADTimeoutError("Timeout error"),
        ]

        for non_api_error in non_api_errors:
            try:
                raise non_api_error
            except KittyCADAPIError:
                pytest.fail(
                    f"Incorrectly caught {type(non_api_error).__name__} as KittyCADAPIError"
                )
            except KittyCADError:
                # Should still be caught as base KittyCADError
                pass


if __name__ == "__main__":
    pytest.main([__file__])
