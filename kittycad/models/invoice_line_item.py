from typing import Dict, Optional

from ..models.currency import Currency
from .base import KittyCadBaseModel


class InvoiceLineItem(KittyCadBaseModel):
    """An invoice line item."""

    amount: float = 0.0

    currency: Currency = "usd"  # type: ignore[assignment]

    description: Optional[str] = None

    id: Optional[str] = None

    invoice_item: Optional[str] = None

    metadata: Dict[str, str] = {}
