from typing import Optional

from ..models.edge_info import EdgeInfo
from .base import KittyCadBaseModel


class AdjacencyInfo(KittyCadBaseModel):
    """Edge info struct (useful for maintaining mappings between edges and faces and adjacent/opposite edges)."""

    adjacent_info: Optional[EdgeInfo] = None

    opposite_info: Optional[EdgeInfo] = None

    original_info: Optional[EdgeInfo] = None
