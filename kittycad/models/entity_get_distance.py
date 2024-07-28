import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.length_unit import LengthUnit
from .base64data import Base64Data


class EntityGetDistance(BaseModel):
    """The response from the `EntitiesGetDistance` command."""

    max_distance: LengthUnit

    min_distance: LengthUnit

    model_config = ConfigDict(protected_namespaces=())
