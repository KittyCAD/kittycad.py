import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class Coupon(BaseModel):
    """The resource representing a Coupon."""

    amount_off: Optional[float] = None

    deleted: Optional[bool] = None

    id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    percent_off: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
