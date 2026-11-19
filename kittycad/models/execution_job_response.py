import datetime
from typing import Optional

from ..models.execution_job_status import ExecutionJobStatus
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ExecutionJobResponse(KittyCadBaseModel):
    """Small lifecycle summary. Fetch immutable inputs explicitly via `/specification`."""

    active_attempt: int

    completed_at: Optional[datetime.datetime] = None

    compute_profile_id: str

    created_at: datetime.datetime

    execution_ended_at: Optional[datetime.datetime] = None

    id: Uuid

    runtime_id: str

    started_at: Optional[datetime.datetime] = None

    state_version: int

    status: ExecutionJobStatus

    timeout_seconds: int

    updated_at: datetime.datetime
