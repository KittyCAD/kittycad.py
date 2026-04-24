from typing import List

from .base import KittyCadBaseModel


class SurfaceCreated(KittyCadBaseModel):
    """Details of a surface that was created under some body."""

    from_segments: List[str]

    id: str

    primitive_face_index: int
