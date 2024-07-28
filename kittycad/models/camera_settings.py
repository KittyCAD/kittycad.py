import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.point3d import Point3d
from ..models.point4d import Point4d
from .base64data import Base64Data


class CameraSettings(BaseModel):
    """Camera settings including position, center, fov etc"""

    center: Point3d

    fov_y: Optional[float] = None

    orientation: Point4d

    ortho: bool

    ortho_scale: Optional[float] = None

    pos: Point3d

    up: Point3d

    model_config = ConfigDict(protected_namespaces=())
