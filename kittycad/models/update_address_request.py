from ..models.address_contact import AddressContact
from ..models.address_details import AddressDetails
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class UpdateAddressRequest(KittyCadBaseModel):
    """Replace a delivery card without changing revisions already used by orders."""

    contact: AddressContact

    expected_revision: Uuid

    is_default_shipping: bool

    label: str

    postal: AddressDetails
