import datetime
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.address_details import AddressDetails
from ..models.currency import Currency


class Customer(BaseModel):
    """The resource representing a payment \"Customer\"."""

    address: Optional[AddressDetails] = None

    balance: float = 0.0

    created_at: datetime.datetime

    currency: Currency = "usd"

    delinquent: bool = False

    email: Optional[str] = None

    id: Optional[str] = None

    metadata: Dict[str, str] = {}

    name: Optional[str] = None

    phone: str = ""

    model_config = ConfigDict(protected_namespaces=())
