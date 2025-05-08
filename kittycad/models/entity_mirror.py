from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.face_edge_info import FaceEdgeInfo


class EntityMirror(BaseModel):
    """The response from the `EntityMirror` endpoint."""

    entity_face_edge_ids: Optional[List[FaceEdgeInfo]] = None

    entity_ids: Optional[List[str]] = None

    model_config = ConfigDict(protected_namespaces=())
