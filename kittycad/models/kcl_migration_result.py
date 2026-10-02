from typing import Dict, Optional

from ..models.kcl_migration_status import KclMigrationStatus
from ..models.kcl_migration_validation import KclMigrationValidation
from .base import KittyCadBaseModel


class KclMigrationResult(KittyCadBaseModel):
    """A worker's terminal candidate, held separately from ordinary project edits."""

    conversion_not_started: Optional[bool] = False

    detail: str

    files: Optional[Dict[str, bytes]] = {}

    status: KclMigrationStatus

    validation: Optional[KclMigrationValidation] = None
