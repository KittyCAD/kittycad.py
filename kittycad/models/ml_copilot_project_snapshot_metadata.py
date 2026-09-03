from typing import Optional

from ..models.ml_copilot_project_revision import MlCopilotProjectRevision
from .base import KittyCadBaseModel


class MlCopilotProjectSnapshotMetadata(KittyCadBaseModel):
    """Revision metadata for the complete `current_files` map in a client message."""

    base_revision: Optional[MlCopilotProjectRevision] = None

    project_id: str

    snapshot_id: str
