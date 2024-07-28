import datetime
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_status import ApiCallStatus
from ..models.async_api_call_type import AsyncApiCallType
from ..models.uuid import Uuid


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
