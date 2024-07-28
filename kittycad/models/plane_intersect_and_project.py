import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.point2d import Point2d
from .base64data import Base64Data


class PlaneIntersectAndProject(BaseModel):
    """Corresponding coordinates of given window coordinates, intersected on given plane."""

    plane_coordinates: Optional[Point2d] = None

    model_config = ConfigDict(protected_namespaces=())
