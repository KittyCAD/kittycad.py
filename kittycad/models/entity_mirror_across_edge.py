from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.face_edge_info import FaceEdgeInfo


class EntityMirrorAcrossEdge(BaseModel):
    """The response from the `EntityMirrorAcrossEdge` endpoint."""

    entity_face_edge_ids: Optional[List[FaceEdgeInfo]] = None

    model_config = ConfigDict(protected_namespaces=())
