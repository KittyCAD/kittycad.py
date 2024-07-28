import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.axis import Axis
from ..models.direction import Direction
from .base64data import Base64Data


class AxisDirectionPair(BaseModel):
    """An [`Axis`] paired with a [`Direction`]."""

    axis: Axis

    direction: Direction

    model_config = ConfigDict(protected_namespaces=())
