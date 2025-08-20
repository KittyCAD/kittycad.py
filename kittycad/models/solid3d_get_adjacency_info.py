from typing import List

from ..models.adjacency_info import AdjacencyInfo
from .base import KittyCadBaseModel


class Solid3dGetAdjacencyInfo(KittyCadBaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces) This includes the opposite and adjacent faces and edges."""

    edges: List[AdjacencyInfo]
