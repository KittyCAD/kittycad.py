import datetime

from ..models.address_contact import AddressContact
from ..models.address_postal_response import AddressPostalResponse
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class AddressResponse(KittyCadBaseModel):
    """One address-book card and its current immutable contents."""

    can_manage: bool

    contact: AddressContact

    created_at: datetime.datetime

    id: Uuid

    is_billing: bool

    is_default_shipping: bool

    is_saved: bool

    label: str

    postal: AddressPostalResponse

    revision_id: Uuid

    updated_at: datetime.datetime
