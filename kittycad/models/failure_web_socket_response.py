import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.api_error import ApiError
from .base64data import Base64Data


class FailureWebSocketResponse(BaseModel):
    """Unsuccessful Websocket response."""

    errors: List[ApiError]

    request_id: Optional[str] = None

    success: bool

    model_config = ConfigDict(protected_namespaces=())
