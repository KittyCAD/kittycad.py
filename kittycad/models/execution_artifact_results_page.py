from typing import List, Optional

from ..models.execution_artifact import ExecutionArtifact
from .base import KittyCadBaseModel


class ExecutionArtifactResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ExecutionArtifact]

    next_page: Optional[str] = None
