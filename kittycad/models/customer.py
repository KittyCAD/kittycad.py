import datetime
from typing import Dict, Optional

from pydantic import BaseModel

from ..models.currency import Currency
from ..models.new_address import NewAddress


class Customer(BaseModel):
    """The resource representing a payment "Customer"."""

    address: Optional[NewAddress] = None

    balance: Optional[float] = None

    created_at: datetime.datetime

    currency: Optional[Currency] = None

    delinquent: Optional[bool] = None

    email: Optional[str] = None

    id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    phone: Optional[str] = None
