from typing import Optional

from ..models.address_contact import AddressContact
from ..models.address_details import AddressDetails
from .base import KittyCadBaseModel


class CreateAddressRequest(KittyCadBaseModel):
    """Create a saved card or an owned one-off destination. Billing is unchanged."""

    contact: AddressContact

    is_default_shipping: Optional[bool] = False

    is_saved: Optional[bool] = True

    label: Optional[str] = ""

    postal: AddressDetails
