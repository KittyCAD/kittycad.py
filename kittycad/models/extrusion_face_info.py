import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.extrusion_face_cap_type import ExtrusionFaceCapType
from .base64data import Base64Data


class ExtrusionFaceInfo(BaseModel):
    """Extrusion face info struct (useful for maintaining mappings between source path segment ids and extrusion faces)"""

    cap: ExtrusionFaceCapType

    curve_id: Optional[str] = None

    face_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
