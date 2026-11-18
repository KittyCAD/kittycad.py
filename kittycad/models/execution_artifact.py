from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ExecutionArtifact(KittyCadBaseModel):
    """Public metadata, without internal bucket/key or routing identity."""

    byte_length: int

    id: Uuid

    path: str

    sha256: str
