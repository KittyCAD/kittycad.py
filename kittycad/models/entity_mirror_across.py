from typing import List, Optional

from ..models.face_edge_info import FaceEdgeInfo
from .base import KittyCadBaseModel


class EntityMirrorAcross(KittyCadBaseModel):
    """The response from the `EntityMirrorAcross` endpoint."""

    entity_face_edge_ids: Optional[List[FaceEdgeInfo]] = None
