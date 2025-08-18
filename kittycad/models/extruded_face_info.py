from typing import List, Optional

from ..models.side_face import SideFace
from .base import KittyCadBaseModel


class ExtrudedFaceInfo(KittyCadBaseModel):
    """IDs for the extruded faces."""

    bottom: Optional[str] = None

    sides: List[SideFace]

    top: str
