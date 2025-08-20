from typing import List

from .base import KittyCadBaseModel


class EntityGetAllChildUuids(KittyCadBaseModel):
    """The response from the `EntityGetAllChildUuids` command."""

    entity_ids: List[str]
