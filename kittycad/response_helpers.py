"""Helper functions for handling API responses."""

import functools
from typing import Callable, Optional, TypeVar

import httpx

from .exceptions import (
    KittyCADAPIError,
    KittyCADClientError,
    KittyCADConnectionError,
    KittyCADServerError,
    KittyCADTimeoutError,
)

T = TypeVar("T")


def raise_for_status(response: httpx.Response) -> None:
    """Raise appropriate KittyCAD exceptions for HTTP error status codes."""
    if response.is_success:
        return

    # Try to parse error details from response
    error_message = f"HTTP {response.status_code}"
    error_code = None
    request_id = None

    # Get status code text for better context
    status_text = {
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        409: "Conflict",
        422: "Unprocessable Entity",
        429: "Too Many Requests",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
    }.get(response.status_code, response.reason_phrase or "Unknown Error")

    try:
        if response.headers.get("content-type", "").startswith("application/json"):
            error_data = response.json()
            if isinstance(error_data, dict):
                api_message = error_data.get("message", "")
                error_code = error_data.get("error_code")
                request_id = error_data.get("request_id")

                # Construct a meaningful error message
                if api_message:
                    error_message = (
                        f"{response.status_code} {status_text}: {api_message}"
                    )
                else:
                    error_message = f"{response.status_code} {status_text}"
            else:
                error_message = f"{response.status_code} {status_text}"
    except Exception:
        # If we can't parse the error response, use the status text
        error_message = f"{response.status_code} {status_text}"

    # Extract request_id from headers if not in body
    if not request_id:
        request_id = response.headers.get("x-request-id")

    # Add context about the request
    url_context = (
        f" (request to {response.request.method} {response.url})"
        if response.request
        else ""
    )
    error_message = error_message + url_context

    # Extract request method and URL for context
    request_method = response.request.method if response.request else None
    request_url = str(response.url) if response.url else None

    # Raise appropriate exception based on status code
    if 400 <= response.status_code < 500:
        raise KittyCADClientError(
            message=error_message,
            status_code=response.status_code,
            error_code=error_code,
            request_id=request_id,
            headers=dict(response.headers),
            request_method=request_method,
            request_url=request_url,
        )
    elif 500 <= response.status_code < 600:
        raise KittyCADServerError(
            message=error_message,
            status_code=response.status_code,
            error_code=error_code,
            request_id=request_id,
            headers=dict(response.headers),
            request_method=request_method,
            request_url=request_url,
        )
    else:
        raise KittyCADAPIError(
            message=error_message,
            status_code=response.status_code,
            error_code=error_code,
            request_id=request_id,
            headers=dict(response.headers),
            request_method=request_method,
            request_url=request_url,
        )


def parse_response_or_raise(
    response: httpx.Response, success_parser=None
) -> Optional[T]:
    """Parse response content or raise appropriate exceptions.

    Args:
        response: The HTTP response
        success_parser: Optional function to parse successful response content

    Returns:
        Parsed response content for successful responses

    Raises:
        KittyCADAPIError: For HTTP error status codes
    """
    # First check for HTTP errors and raise exceptions
    raise_for_status(response)

    # For successful responses, parse the content if a parser is provided
    if success_parser:
        return success_parser()

    return None


def wrap_httpx_exceptions(
    request_method: Optional[str] = None,
    request_url: Optional[str] = None,
):
    """Decorator factory to wrap HTTPX exceptions in KittyCAD exceptions.

    Args:
        request_method: HTTP method for context (if known)
        request_url: Request URL for context (if known)

    Returns:
        Decorator function that wraps HTTPX exceptions
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except httpx.TimeoutException as e:
                # Extract timeout info if available
                timeout_seconds = None
                if hasattr(e, "timeout") and e.timeout:
                    timeout_seconds = float(e.timeout)

                raise KittyCADTimeoutError(
                    message=f"Request timed out: {str(e)}",
                    timeout_seconds=timeout_seconds,
                    request_method=request_method,
                    request_url=request_url,
                ) from e

            except httpx.ConnectError as e:
                raise KittyCADConnectionError(
                    message=f"Connection failed: {str(e)}",
                    original_error=e,
                    request_method=request_method,
                    request_url=request_url,
                ) from e

            except httpx.NetworkError as e:
                # NetworkError is a broader category that includes ConnectError
                # Handle other network errors not caught above
                if isinstance(e, httpx.ConnectError):
                    # This should already be handled above, but just in case
                    raise KittyCADConnectionError(
                        message=f"Connection failed: {str(e)}",
                        original_error=e,
                        request_method=request_method,
                        request_url=request_url,
                    ) from e
                else:
                    raise KittyCADConnectionError(
                        message=f"Network error: {str(e)}",
                        original_error=e,
                        request_method=request_method,
                        request_url=request_url,
                    ) from e

            except httpx.RequestError as e:
                # Generic request error fallback
                # This catches other HTTPX errors not specifically handled above
                raise KittyCADConnectionError(
                    message=f"Request error: {str(e)}",
                    original_error=e,
                    request_method=request_method,
                    request_url=request_url,
                ) from e

        return wrapper

    return decorator


def wrap_httpx_exceptions_async(
    request_method: Optional[str] = None,
    request_url: Optional[str] = None,
):
    """Async decorator factory to wrap HTTPX exceptions in KittyCAD exceptions.

    Args:
        request_method: HTTP method for context (if known)
        request_url: Request URL for context (if known)

    Returns:
        Async decorator function that wraps HTTPX exceptions
    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except httpx.TimeoutException as e:
                # Extract timeout info if available
                timeout_seconds = None
                if hasattr(e, "timeout") and e.timeout:
                    timeout_seconds = float(e.timeout)

                raise KittyCADTimeoutError(
                    message=f"Request timed out: {str(e)}",
                    timeout_seconds=timeout_seconds,
                    request_method=request_method,
                    request_url=request_url,
                ) from e

            except httpx.ConnectError as e:
                raise KittyCADConnectionError(
                    message=f"Connection failed: {str(e)}",
                    original_error=e,
                    request_method=request_method,
                    request_url=request_url,
                ) from e

            except httpx.NetworkError as e:
                # NetworkError is a broader category that includes ConnectError
                # Handle other network errors not caught above
                if isinstance(e, httpx.ConnectError):
                    # This should already be handled above, but just in case
                    raise KittyCADConnectionError(
                        message=f"Connection failed: {str(e)}",
                        original_error=e,
                        request_method=request_method,
                        request_url=request_url,
                    ) from e
                else:
                    raise KittyCADConnectionError(
                        message=f"Network error: {str(e)}",
                        original_error=e,
                        request_method=request_method,
                        request_url=request_url,
                    ) from e

            except httpx.RequestError as e:
                # Generic request error fallback
                # This catches other HTTPX errors not specifically handled above
                raise KittyCADConnectionError(
                    message=f"Request error: {str(e)}",
                    original_error=e,
                    request_method=request_method,
                    request_url=request_url,
                ) from e

        return wrapper

    return decorator


def make_request_with_error_handling(
    http_client: httpx.Client, method: str, url: str, **kwargs
) -> httpx.Response:
    """Make an HTTP request with comprehensive error handling.

    Args:
        http_client: HTTPX client instance
        method: HTTP method (GET, POST, etc.)
        url: Request URL
        **kwargs: Additional arguments passed to the HTTP method

    Returns:
        HTTP response object

    Raises:
        KittyCADTimeoutError: For timeout errors
        KittyCADConnectionError: For network/connection errors
        KittyCADClientError: For 4xx HTTP errors
        KittyCADServerError: For 5xx HTTP errors
        KittyCADAPIError: For other HTTP errors
    """

    @wrap_httpx_exceptions(request_method=method.upper(), request_url=url)
    def _make_request():
        # Get the appropriate method from the client
        client_method = getattr(http_client, method.lower())
        return client_method(url, **kwargs)

    # Make the request (may raise KittyCAD*Error)
    response = _make_request()

    # Check for HTTP errors and raise appropriate exceptions
    raise_for_status(response)

    return response


async def make_async_request_with_error_handling(
    http_client: httpx.AsyncClient, method: str, url: str, **kwargs
) -> httpx.Response:
    """Make an async HTTP request with comprehensive error handling.

    Args:
        http_client: HTTPX async client instance
        method: HTTP method (GET, POST, etc.)
        url: Request URL
        **kwargs: Additional arguments passed to the HTTP method

    Returns:
        HTTP response object

    Raises:
        KittyCADTimeoutError: For timeout errors
        KittyCADConnectionError: For network/connection errors
        KittyCADClientError: For 4xx HTTP errors
        KittyCADServerError: For 5xx HTTP errors
        KittyCADAPIError: For other HTTP errors
    """

    @wrap_httpx_exceptions_async(request_method=method.upper(), request_url=url)
    async def _make_request():
        # Get the appropriate method from the client
        client_method = getattr(http_client, method.lower())
        return await client_method(url, **kwargs)

    # Make the request (may raise KittyCAD*Error)
    response = await _make_request()

    # Check for HTTP errors and raise appropriate exceptions
    raise_for_status(response)

    return response
