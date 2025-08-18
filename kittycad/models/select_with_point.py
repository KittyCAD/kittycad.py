from typing import Optional

from .base import KittyCadBaseModel


class SelectWithPoint(KittyCadBaseModel):
    """The response from the `SelectWithPoint` command."""

    entity_id: Optional[str] = None
