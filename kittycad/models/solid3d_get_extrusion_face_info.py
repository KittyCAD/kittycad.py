from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.extrusion_face_info import ExtrusionFaceInfo


class Solid3dgetextrusionfaceinfo(BaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces)"""

    faces: List[ExtrusionFaceInfo]

    model_config = ConfigDict(protected_namespaces=())
