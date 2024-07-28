import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.unit_mass import UnitMass
from .base64data import Base64Data


class Mass(BaseModel):
    """The mass response."""

    mass: float

    output_unit: UnitMass

    model_config = ConfigDict(protected_namespaces=())
