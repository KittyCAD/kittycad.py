import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.length_unit import LengthUnit
from .base64data import Base64Data


class Point2d(BaseModel):
    """A point in 2D space"""

    x: LengthUnit

    y: LengthUnit

    model_config = ConfigDict(protected_namespaces=())
