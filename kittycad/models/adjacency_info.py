from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.edge_info import EdgeInfo


class AdjacencyInfo(BaseModel):
    """Edge info struct (useful for maintaining mappings between edges and faces and adjacent/opposite edges)."""

    adjacent_info: Optional[EdgeInfo] = None

    opposite_info: Optional[EdgeInfo] = None

    original_info: Optional[EdgeInfo] = None

    model_config = ConfigDict(protected_namespaces=())
