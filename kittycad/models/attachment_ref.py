from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class AttachmentRef(KittyCadBaseModel):
    """Coordinates for fetching a persisted attachment on demand."""

    content_hash: Optional[str] = None

    index: int

    prompt_id: Uuid

    seq: int
