import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.country_code import CountryCode
from .base64data import Base64Data


class AddressDetails(BaseModel):
    """Address details."""

    city: Optional[str] = None

    country: CountryCode

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None

    zip: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
