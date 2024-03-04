import datetime
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.address_details import AddressDetails
from ..models.currency import Currency


class Customer(BaseModel):
    """The resource representing a payment \"Customer\"."""

    address: Optional[AddressDetails] = None

    balance: Optional[float] = None

    created_at: datetime.datetime

    currency: Optional[Currency] = None

    delinquent: Optional[bool] = None

    email: Optional[str] = None

    id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
