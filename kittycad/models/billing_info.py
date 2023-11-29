from typing import Optional

from pydantic import BaseModel
from pydantic_extra_types.phone_number import PhoneNumber

from ..models.new_address import NewAddress


class BillingInfo(BaseModel):
    """The billing information for payments."""

    address: Optional[NewAddress] = None

    name: Optional[str] = None

    phone: Optional[PhoneNumber] = None
