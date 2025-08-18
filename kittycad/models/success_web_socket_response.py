from typing import Optional

from ..models.ok_web_socket_response_data import OkWebSocketResponseData
from .base import KittyCadBaseModel


class SuccessWebSocketResponse(KittyCadBaseModel):
    """Successful Websocket response."""

    request_id: Optional[str] = None

    resp: OkWebSocketResponseData

    success: bool
