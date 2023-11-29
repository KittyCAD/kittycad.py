from typing import Optional

from pydantic import BaseModel

from ..models.new_address import NewAddress


class BillingInfo(BaseModel):
    """The billing information for payments."""

    address: Optional[NewAddress] = None

    name: Optional[str] = None

    phone: Optional[str] = None
