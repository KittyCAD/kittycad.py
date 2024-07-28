import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class PerspectiveCameraParameters(BaseModel):
    """Defines a perspective view."""

    fov_y: Optional[float] = None

    z_far: Optional[float] = None

    z_near: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
