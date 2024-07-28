import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.api_call_status import ApiCallStatus
from ..models.async_api_call_type import AsyncApiCallType
from ..models.uuid import Uuid
from .base64data import Base64Data


class AsyncApiCall(BaseModel):
    """An async API call."""

    completed_at: Optional[datetime.datetime] = None

    created_at: datetime.datetime

    error: Optional[str] = None

    id: Uuid

    input: Optional[Any] = None

    output: Optional[Any] = None

    started_at: Optional[datetime.datetime] = None

    status: ApiCallStatus

    type: AsyncApiCallType

    updated_at: datetime.datetime

    user_id: Uuid

    worker: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
