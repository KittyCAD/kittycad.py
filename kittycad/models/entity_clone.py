from typing import List, Optional

from ..models.face_edge_info import FaceEdgeInfo
from .base import KittyCadBaseModel


class EntityClone(KittyCadBaseModel):
    """The response from the `EntityClone` command."""

    face_edge_ids: Optional[List[FaceEdgeInfo]] = None
