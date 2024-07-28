import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.point3d import Point3d
from ..models.unit_length import UnitLength
from .base64data import Base64Data


class CenterOfMass(BaseModel):
    """The center of mass response."""

    center_of_mass: Point3d

    output_unit: UnitLength

    model_config = ConfigDict(protected_namespaces=())
