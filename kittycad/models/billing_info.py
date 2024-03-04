from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.address_details import AddressDetails


class BillingInfo(BaseModel):
    """The billing information for payments."""

    address: Optional[AddressDetails] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
