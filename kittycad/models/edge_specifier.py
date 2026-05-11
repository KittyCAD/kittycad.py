from typing import List, Optional

from .base import KittyCadBaseModel


class EdgeSpecifier(KittyCadBaseModel):
    """An edge can be referenced by its uuid or by the faces that uniquely define it."""

    end_faces: Optional[List[str]] = None

    index: Optional[int] = None

    side_faces: List[str]
