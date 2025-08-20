from typing import List

from .base import KittyCadBaseModel


class FaceEdgeInfo(KittyCadBaseModel):
    """Faces and edges id info (most used in identifying geometry in patterned and mirrored objects)."""

    edges: List[str]

    faces: List[str]

    object_id: str
