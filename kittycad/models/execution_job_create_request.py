from typing import Dict, List, Optional

from ..models.execution_job_input import ExecutionJobInput
from ..models.execution_job_output import ExecutionJobOutput
from .base import KittyCadBaseModel


class ExecutionJobCreateRequest(KittyCadBaseModel):
    """Request to create an asynchronous execution job."""

    command: List[str]

    compute_profile_id: str

    environment: Optional[Dict[str, str]] = {}

    inputs: Optional[List[ExecutionJobInput]] = []

    outputs: Optional[List[ExecutionJobOutput]] = []

    runtime_id: str

    timeout_seconds: int
