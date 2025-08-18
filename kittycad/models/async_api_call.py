import datetime
from typing import Any, Optional

from ..models.api_call_status import ApiCallStatus
from ..models.async_api_call_type import AsyncApiCallType
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class AsyncApiCall(KittyCadBaseModel):
    """An async API call."""

    attempts: int = 0

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
