from typing import List

from .base import KittyCadBaseModel


class PathGetVertexUuids(KittyCadBaseModel):
    """The response from the `PathGetVertexUuids` command."""

    vertex_ids: List[str]
