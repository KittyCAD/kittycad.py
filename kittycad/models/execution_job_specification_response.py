from typing import List

from ..models.execution_job_input import ExecutionJobInput
from ..models.execution_job_output import ExecutionJobOutput
from .base import KittyCadBaseModel


class ExecutionJobSpecificationResponse(KittyCadBaseModel):
    """Immutable customer-facing specification, excluding environment values and internal routing."""

    command: List[str]

    compute_profile_id: str

    inputs: List[ExecutionJobInput]

    outputs: List[ExecutionJobOutput]

    runtime_id: str

    timeout_seconds: int
