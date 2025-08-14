from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.adjacency_info import AdjacencyInfo


class Solid3dGetAdjacencyInfo(BaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces) This includes the opposite and adjacent faces and edges."""

    edges: List[AdjacencyInfo]

    model_config = ConfigDict(protected_namespaces=())
