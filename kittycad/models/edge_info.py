from typing import List

from .base import KittyCadBaseModel


class EdgeInfo(KittyCadBaseModel):
    """A list of faces for a specific edge."""

    edge_id: str

    faces: List[str]
