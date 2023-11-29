from typing import List, Optional

from pydantic import BaseModel

from ..models.api_error import ApiError


class FailureWebSocketResponse(BaseModel):
    """Unsuccessful Websocket response."""

    errors: List[ApiError]

    request_id: Optional[str] = None

    success: bool
