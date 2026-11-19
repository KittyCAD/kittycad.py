from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ExecutionJobInput(KittyCadBaseModel):
    """An input artifact staged at a relative path before execution."""

    artifact_id: Uuid

    path: str
