from typing import List, Optional

from ..models.api_error import ApiError
from .base import KittyCadBaseModel


class FailureWebSocketResponse(KittyCadBaseModel):
    """Unsuccessful Websocket response."""

    errors: List[ApiError]

    request_id: Optional[str] = None

    success: bool
