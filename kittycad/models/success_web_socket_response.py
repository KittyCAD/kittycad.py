from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.ok_web_socket_response_data import OkWebSocketResponseData


class SuccessWebSocketResponse(BaseModel):
    """Successful Websocket response."""

    request_id: Optional[str] = None

    resp: OkWebSocketResponseData

    success: bool

    model_config = ConfigDict(protected_namespaces=())
