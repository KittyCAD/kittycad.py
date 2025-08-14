from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.face_edge_info import FaceEdgeInfo


class EntityCircularPattern(BaseModel):
    """The response from the `EntityCircularPattern` command."""

    entity_face_edge_ids: Optional[List[FaceEdgeInfo]] = None

    model_config = ConfigDict(protected_namespaces=())
