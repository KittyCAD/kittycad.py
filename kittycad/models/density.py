import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.unit_density import UnitDensity
from .base64data import Base64Data


class Density(BaseModel):
    """The density response."""

    density: float

    output_unit: UnitDensity

    model_config = ConfigDict(protected_namespaces=())
