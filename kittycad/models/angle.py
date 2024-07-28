import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.unit_angle import UnitAngle
from .base64data import Base64Data


class Angle(BaseModel):
    """An angle, with a specific unit."""

    unit: UnitAngle

    value: float

    model_config = ConfigDict(protected_namespaces=())
