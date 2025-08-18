from typing import Optional

from .base import KittyCadBaseModel


class HighlightSetEntity(KittyCadBaseModel):
    """The response from the `HighlightSetEntity` command."""

    entity_id: Optional[str] = None

    sequence: Optional[int] = None
