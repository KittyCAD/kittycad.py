from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.currency import Currency


class InvoiceLineItem(BaseModel):
    """An invoice line item."""

    amount: Optional[float] = None

    currency: Optional[Currency] = None

    description: Optional[str] = None

    id: Optional[str] = None

    invoice_item: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    model_config = ConfigDict(protected_namespaces=())
