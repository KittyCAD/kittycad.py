import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class DiscountCode(BaseModel):
    """A discount code for a store."""

    code: str

    expires_at: Optional[datetime.datetime] = None

    percent_off: int

    model_config = ConfigDict(protected_namespaces=())
