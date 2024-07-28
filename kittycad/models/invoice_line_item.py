import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.currency import Currency
from .base64data import Base64Data


class InvoiceLineItem(BaseModel):
    """An invoice line item."""

    amount: Optional[float] = None

    currency: Optional[Currency] = None

    description: Optional[str] = None

    id: Optional[str] = None

    invoice_item: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    model_config = ConfigDict(protected_namespaces=())
