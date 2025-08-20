from typing import List

from .base import KittyCadBaseModel


class AddHoleFromOffset(KittyCadBaseModel):
    """The response from the `AddHoleFromOffset` command."""

    entity_ids: List[str]
