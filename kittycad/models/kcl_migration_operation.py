import datetime
from typing import Optional

from ..models.kcl_migration_result import KclMigrationResult
from ..models.kcl_migration_status import KclMigrationStatus
from ..models.kcl_migration_target import KclMigrationTarget
from ..models.ml_copilot_project_snapshot_metadata import (
    MlCopilotProjectSnapshotMetadata,
)
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class KclMigrationOperation(KittyCadBaseModel):
    """Persisted operation state, safe to retrieve again without starting new work."""

    deadline: datetime.datetime

    id: Uuid

    project_snapshot: MlCopilotProjectSnapshotMetadata

    result: Optional[KclMigrationResult] = None

    status: KclMigrationStatus

    target: KclMigrationTarget
