import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.point3d import Point3d
from .base64data import Base64Data


class LinearTransform(BaseModel):
    """Ways to transform each solid being replicated in a repeating pattern."""

    replicate: Optional[bool] = None

    scale: Optional[Point3d] = None

    translate: Optional[Point3d] = None

    model_config = ConfigDict(protected_namespaces=())
