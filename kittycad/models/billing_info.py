import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.address_details import AddressDetails
from .base64data import Base64Data


class BillingInfo(BaseModel):
    """The billing information for payments."""

    address: Optional[AddressDetails] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
