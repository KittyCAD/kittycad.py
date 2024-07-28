import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.curve_type import CurveType
from .base64data import Base64Data


class CurveGetType(BaseModel):
    """The response from the `CurveGetType` command."""

    curve_type: CurveType

    model_config = ConfigDict(protected_namespaces=())
