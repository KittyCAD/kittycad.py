from typing import Dict, Optional

from ..models.kcl_migration_target import KclMigrationTarget
from ..models.ml_copilot_project_snapshot_metadata import (
    MlCopilotProjectSnapshotMetadata,
)
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class KclMigrationRequest(KittyCadBaseModel):
    """A complete, immutable input snapshot. It does not grant sponsorship itself."""

    allow_preview: Optional[bool] = False

    current_files: Dict[str, bytes]

    entrypoint: str

    project_snapshot: MlCopilotProjectSnapshotMetadata

    request_id: Uuid

    target: KclMigrationTarget
