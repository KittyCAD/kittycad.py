from typing import List

from ..models.execution_input_artifact import ExecutionInputArtifact
from .base import KittyCadBaseModel


class ExecutionInputBatch(KittyCadBaseModel):
    """Inputs from a multipart upload, in request order."""

    artifacts: List[ExecutionInputArtifact]
