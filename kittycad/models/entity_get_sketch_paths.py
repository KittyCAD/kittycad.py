from typing import List

from .base import KittyCadBaseModel


class EntityGetSketchPaths(KittyCadBaseModel):
    """The response from the `EntityGetSketchPaths` command."""

    entity_ids: List[str]
