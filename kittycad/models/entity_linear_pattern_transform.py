from typing import List, Optional

from ..models.face_edge_info import FaceEdgeInfo
from .base import KittyCadBaseModel


class EntityLinearPatternTransform(KittyCadBaseModel):
    """The response from the `EntityLinearPatternTransform` command."""

    entity_face_edge_ids: Optional[List[FaceEdgeInfo]] = None
