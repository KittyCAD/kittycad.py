from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ExecutionInputArtifact(KittyCadBaseModel):
    """An uploaded input and the filename supplied for a multipart upload."""

    byte_length: int

    id: Uuid

    path: Optional[str] = None

    sha256: str
