import datetime
from typing import Dict, Optional

from ..models.address_details import AddressDetails
from ..models.currency import Currency
from .base import KittyCadBaseModel


class Customer(KittyCadBaseModel):
    """The resource representing a payment \"Customer\"."""

    address: Optional[AddressDetails] = None

    balance: Optional[float] = 0.0

    created_at: datetime.datetime

    currency: Optional[Currency] = "usd"  # type: ignore[assignment]

    delinquent: Optional[bool] = False

    email: Optional[str] = None

    id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = {}

    name: Optional[str] = None

    phone: Optional[str] = ""
