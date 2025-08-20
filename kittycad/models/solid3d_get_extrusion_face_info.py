from typing import List

from ..models.extrusion_face_info import ExtrusionFaceInfo
from .base import KittyCadBaseModel


class Solid3dGetExtrusionFaceInfo(KittyCadBaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces)"""

    faces: List[ExtrusionFaceInfo]
