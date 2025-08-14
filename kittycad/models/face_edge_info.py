from typing import List

from pydantic import BaseModel, ConfigDict


class FaceEdgeInfo(BaseModel):
    """Faces and edges id info (most used in identifying geometry in patterned and mirrored objects)."""

    edges: List[str]

    faces: List[str]

    object_id: str

    model_config = ConfigDict(protected_namespaces=())
