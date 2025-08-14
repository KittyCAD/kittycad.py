from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.address_details import AddressDetails


class Billinginfo(BaseModel):
    """The billing information for payments."""

    address: Optional[AddressDetails] = None

    name: Optional[str] = None

    phone: str = ""

    model_config = ConfigDict(protected_namespaces=())
