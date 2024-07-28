import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.unit_volume import UnitVolume
from .base64data import Base64Data


class Volume(BaseModel):
    """The volume response."""

    output_unit: UnitVolume

    volume: float

    model_config = ConfigDict(protected_namespaces=())
