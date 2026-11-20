from typing import Optional

from ..models.address_contact import AddressContact
from ..models.address_details import AddressDetails
from .base import KittyCadBaseModel


class AddressContent(KittyCadBaseModel):
    """Address contents. Ownership, saved-address labels, and shipping speed are separate."""

    contact: Optional[AddressContact] = {"company": "", "phone": "", "recipient": ""}  # type: ignore[assignment]

    postal: AddressDetails
