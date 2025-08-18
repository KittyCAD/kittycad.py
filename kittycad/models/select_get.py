from typing import List

from .base import KittyCadBaseModel


class SelectGet(KittyCadBaseModel):
    """The response from the `SelectGet` command."""

    entity_ids: List[str]
