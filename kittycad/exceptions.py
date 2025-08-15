"""KittyCAD API exceptions."""

from typing import Dict, Optional


class KittyCADError(Exception):
    """Base exception for all KittyCAD API errors."""

    def __init__(self, message: str, request_id: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.request_id = request_id

    def __str__(self) -> str:
        if self.request_id:
            return f"{self.message} (request_id: {self.request_id})"
        return self.message


class KittyCADAPIError(KittyCADError):
    """Exception raised for API errors returned by the server."""

    def __init__(
        self,
        message: str,
        status_code: int,
        error_code: Optional[str] = None,
        request_id: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        super().__init__(message, request_id)
        self.status_code = status_code
        self.error_code = error_code
        self.headers = headers or {}

    def __str__(self) -> str:
        base_msg = f"HTTP {self.status_code}: {self.message}"
        if self.error_code:
            base_msg = f"{base_msg} (error_code: {self.error_code})"
        if self.request_id:
            base_msg = f"{base_msg} (request_id: {self.request_id})"
        return base_msg


class KittyCADClientError(KittyCADAPIError):
    """Exception raised for 4xx client errors."""

    pass


class KittyCADServerError(KittyCADAPIError):
    """Exception raised for 5xx server errors."""

    pass


class KittyCADConnectionError(KittyCADError):
    """Exception raised for connection/network related errors."""

    pass


class KittyCADTimeoutError(KittyCADError):
    """Exception raised when a request times out."""

    pass
