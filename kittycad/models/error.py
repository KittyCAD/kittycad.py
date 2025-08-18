from typing import Optional

from .base import KittyCadBaseModel


class Error(KittyCadBaseModel):
    """Error information from a response."""

    error_code: Optional[str] = None

    message: str

    request_id: str
