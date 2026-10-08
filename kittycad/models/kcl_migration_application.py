from ..models.kcl_migration_application_status import KclMigrationApplicationStatus
from .base import KittyCadBaseModel


class KclMigrationApplication(KittyCadBaseModel):
    """A revision-fenced acknowledgement from the client that owns the project files."""

    revision: int

    status: KclMigrationApplicationStatus
