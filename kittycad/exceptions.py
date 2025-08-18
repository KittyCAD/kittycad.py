"""KittyCAD API exceptions."""

from typing import Dict, Optional


class KittyCADError(Exception):
    """Base exception for all KittyCAD API errors.

    Attributes:
        message: Human-readable error message
        request_id: Optional request ID for debugging (when available)
    """

    def __init__(self, message: str, request_id: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.request_id = request_id

    def __str__(self) -> str:
        if self.request_id:
            return f"{self.message} (request_id: {self.request_id})"
        return self.message


class KittyCADAPIError(KittyCADError):
    """Exception raised for API errors returned by the server.

    Attributes:
        message: Human-readable error message
        status_code: HTTP status code
        error_code: API-specific error code (when available)
        request_id: Request ID for debugging (when available)
        headers: Response headers dictionary
        request_method: HTTP method used for the request (when available)
        request_url: URL that was requested (when available)
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        error_code: Optional[str] = None,
        request_id: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        request_method: Optional[str] = None,
        request_url: Optional[str] = None,
    ):
        super().__init__(message, request_id)
        self.status_code = status_code
        self.error_code = error_code
        self.headers = headers or {}
        self.request_method = request_method
        self.request_url = request_url

    def __str__(self) -> str:
        base_msg = f"HTTP {self.status_code}: {self.message}"
        if self.error_code:
            base_msg = f"{base_msg} (error_code: {self.error_code})"
        if self.request_id:
            base_msg = f"{base_msg} (request_id: {self.request_id})"
        return base_msg


class KittyCADClientError(KittyCADAPIError):
    """Exception raised for 4xx client errors.

    These errors typically indicate issues with the request itself,
    such as invalid parameters, authentication problems, or missing permissions.
    """

    pass


class KittyCADServerError(KittyCADAPIError):
    """Exception raised for 5xx server errors.

    These errors indicate issues on the server side,
    such as internal server errors or service unavailability.
    """

    pass


class KittyCADConnectionError(KittyCADError):
    """Exception raised for connection/network related errors.

    This includes DNS resolution failures, connection refused,
    SSL/TLS errors, and other network-level issues.

    Attributes:
        message: Human-readable error message
        request_id: Optional request ID (usually None for connection errors)
        original_error: The original underlying exception that caused this error
        request_method: HTTP method attempted (when available)
        request_url: URL that was being requested (when available)
    """

    def __init__(
        self,
        message: str,
        request_id: Optional[str] = None,
        original_error: Optional[Exception] = None,
        request_method: Optional[str] = None,
        request_url: Optional[str] = None,
    ):
        super().__init__(message, request_id)
        self.original_error = original_error
        self.request_method = request_method
        self.request_url = request_url

    def __str__(self) -> str:
        base_msg = self.message
        if self.request_method and self.request_url:
            base_msg = (
                f"{base_msg} (request to {self.request_method} {self.request_url})"
            )
        if self.request_id:
            base_msg = f"{base_msg} (request_id: {self.request_id})"
        if self.original_error:
            base_msg = f"{base_msg} [caused by: {self.original_error}]"
        return base_msg


class KittyCADTimeoutError(KittyCADError):
    """Exception raised when a request times out.

    This includes both connection timeouts and read timeouts.

    Attributes:
        message: Human-readable error message
        request_id: Optional request ID (usually None for timeout errors)
        timeout_seconds: The timeout value that was exceeded (when available)
        request_method: HTTP method attempted (when available)
        request_url: URL that was being requested (when available)
    """

    def __init__(
        self,
        message: str,
        request_id: Optional[str] = None,
        timeout_seconds: Optional[float] = None,
        request_method: Optional[str] = None,
        request_url: Optional[str] = None,
    ):
        super().__init__(message, request_id)
        self.timeout_seconds = timeout_seconds
        self.request_method = request_method
        self.request_url = request_url

    def __str__(self) -> str:
        base_msg = self.message
        if self.timeout_seconds:
            base_msg = f"{base_msg} (timeout: {self.timeout_seconds}s)"
        if self.request_method and self.request_url:
            base_msg = (
                f"{base_msg} (request to {self.request_method} {self.request_url})"
            )
        if self.request_id:
            base_msg = f"{base_msg} (request_id: {self.request_id})"
        return base_msg
