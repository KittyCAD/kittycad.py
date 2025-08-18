from typing import List

from .base import KittyCadBaseModel


class Solid3dGetAllOppositeEdges(KittyCadBaseModel):
    """The response from the `Solid3dGetAllOppositeEdges` command."""

    edges: List[str]
