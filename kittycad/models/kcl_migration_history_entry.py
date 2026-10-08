import datetime
from typing import Optional

from ..models.kcl_migration_application import KclMigrationApplication
from ..models.kcl_migration_status import KclMigrationStatus
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class KclMigrationHistoryEntry(KittyCadBaseModel):
    """Read-only conversation entry. It contains no files, edits or provider checkpoints."""

    after_prompt_id: Optional[Uuid] = None

    application: KclMigrationApplication

    conversation_id: Uuid

    created_at: datetime.datetime

    detail: str

    operation_id: Uuid

    prompt_id: Optional[Uuid] = None

    status: KclMigrationStatus
