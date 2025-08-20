from typing import Optional

from ..models.extrusion_face_cap_type import ExtrusionFaceCapType
from .base import KittyCadBaseModel


class ExtrusionFaceInfo(KittyCadBaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces)"""

    cap: ExtrusionFaceCapType

    curve_id: Optional[str] = None

    face_id: Optional[str] = None
