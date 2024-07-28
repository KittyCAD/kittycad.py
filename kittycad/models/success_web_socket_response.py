import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.ok_web_socket_response_data import OkWebSocketResponseData
from .base64data import Base64Data


class SuccessWebSocketResponse(BaseModel):
    """Successful Websocket response."""

    request_id: Optional[str] = None

    resp: OkWebSocketResponseData

    success: bool

    model_config = ConfigDict(protected_namespaces=())
