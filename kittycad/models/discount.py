import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.coupon import Coupon
from .base64data import Base64Data


class Discount(BaseModel):
    """The resource representing a Discount."""

    coupon: Coupon

    model_config = ConfigDict(protected_namespaces=())
