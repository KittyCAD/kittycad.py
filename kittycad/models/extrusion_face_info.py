from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.extrusion_face_cap_type import ExtrusionFaceCapType


class ExtrusionFaceInfo(BaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces)"""

    cap: ExtrusionFaceCapType

    curve_id: Optional[str] = None

    face_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
