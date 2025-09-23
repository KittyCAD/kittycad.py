import datetime
from typing import Dict, Optional

from ..models.address_details import AddressDetails
from ..models.currency import Currency
from .base import KittyCadBaseModel


class Customer(KittyCadBaseModel):
    """The resource representing a payment \"Customer\"."""

    address: Optional[AddressDetails] = None

    balance: float = 0.0

    created_at: datetime.datetime

    currency: Currency = "usd"  # type: ignore[assignment]

    delinquent: bool = False

    email: Optional[str] = None

    id: Optional[str] = None

    metadata: Dict[str, str] = {}

    name: Optional[str] = None

    phone: str = ""
