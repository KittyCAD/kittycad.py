from typing import List

from ..models.fraction_of_edge import FractionOfEdge
from .base import KittyCadBaseModel


class SurfaceEdgeReference(KittyCadBaseModel):
    """An object id, that corresponds to a surface body, and a list of edges of the surface."""

    edges: List[FractionOfEdge]

    object_id: str
