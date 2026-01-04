from typing import List

from .base import KittyCadBaseModel


class SceneGetEntityIds(KittyCadBaseModel):
    """The response from the `SceneGetEntityIds` command."""

    entity_ids: List[List[str]]
