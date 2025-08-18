from typing import List

from .base import KittyCadBaseModel


class MakeOffsetPath(KittyCadBaseModel):
    """The response from the `MakeOffsetPath` command."""

    entity_ids: List[str]
