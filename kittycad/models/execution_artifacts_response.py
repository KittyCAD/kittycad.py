from typing import Optional

from ..models.execution_artifact_results_page import ExecutionArtifactResultsPage
from .base import KittyCadBaseModel


class ExecutionArtifactsResponse(KittyCadBaseModel):
    """Archival state and verified complete objects, including partial failure results."""

    artifacts: ExecutionArtifactResultsPage

    failure_code: Optional[str] = None

    state: str
