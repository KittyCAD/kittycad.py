import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.point3d import Point3d
from .base64data import Base64Data


class CurveGetControlPoints(BaseModel):
    """The response from the `CurveGetControlPoints` command."""

    control_points: List[Point3d]

    model_config = ConfigDict(protected_namespaces=())
