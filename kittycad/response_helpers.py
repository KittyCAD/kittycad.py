"""Helper functions for handling API responses."""

from typing import Optional, TypeVar

import httpx

from .exceptions import KittyCADAPIError, KittyCADClientError, KittyCADServerError

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

    # Raise appropriate exception based on status code
    if 400 <= response.status_code < 500:
        raise KittyCADClientError(
            message=error_message,
            status_code=response.status_code,
            error_code=error_code,
            request_id=request_id,
            headers=dict(response.headers),
        )
    elif 500 <= response.status_code < 600:
        raise KittyCADServerError(
            message=error_message,
            status_code=response.status_code,
            error_code=error_code,
            request_id=request_id,
            headers=dict(response.headers),
        )
    else:
        raise KittyCADAPIError(
            message=error_message,
            status_code=response.status_code,
            error_code=error_code,
            request_id=request_id,
            headers=dict(response.headers),
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
