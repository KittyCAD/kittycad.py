from typing import Optional

from .base import KittyCadBaseModel


class AddressContact(KittyCadBaseModel):
    """Delivery contact fields shared by saved addresses and one-off destinations."""

    company: Optional[str] = ""

    phone: Optional[str] = ""

    recipient: Optional[str] = ""
