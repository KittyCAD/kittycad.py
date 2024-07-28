import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.unit_area import UnitArea
from .base64data import Base64Data


class SurfaceArea(BaseModel):
    """The surface area response."""

    output_unit: UnitArea

    surface_area: float

    model_config = ConfigDict(protected_namespaces=())
