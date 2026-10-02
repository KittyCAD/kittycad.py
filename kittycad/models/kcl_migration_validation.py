from ..models.kcl_migration_target import KclMigrationTarget
from .base import KittyCadBaseModel


class KclMigrationValidation(KittyCadBaseModel):
    """Evidence required before a candidate may be returned as successful."""

    behavior_preserved: bool

    geometry_preserved: bool

    rules_revision: str

    runtime_version: str

    source_executed: bool

    source_version: str

    summary: str

    target: KclMigrationTarget

    target_executed: bool
