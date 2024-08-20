from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from ..models.currency import Currency


class InvoiceLineItem(BaseModel):
    """An invoice line item."""

    amount: float = 0.0

    currency: Currency = "usd"

    description: Optional[str] = None

    id: Optional[str] = None

    invoice_item: Optional[str] = None

    metadata: Dict[str, str] = {}

    model_config = ConfigDict(protected_namespaces=())
