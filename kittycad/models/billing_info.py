from typing import Optional

from ..models.address_details import AddressDetails
from .base import KittyCadBaseModel


class BillingInfo(KittyCadBaseModel):
    """The billing information for payments."""

    address: Optional[AddressDetails] = None

    name: Optional[str] = None

    phone: str = ""
