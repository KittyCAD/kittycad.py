import datetime
from typing import Dict, List, Optional

from ..models.currency import Currency
from ..models.discount import Discount
from ..models.invoice_line_item import InvoiceLineItem
from ..models.invoice_status import InvoiceStatus
from .base import KittyCadBaseModel


class Invoice(KittyCadBaseModel):
    """An invoice."""

    amount_due: float = 0.0

    amount_paid: float = 0.0

    amount_remaining: float = 0.0

    attempt_count: int = 0

    attempted: bool = False

    billing_reason: Optional[str] = None

    collection_method: Optional[str] = None

    created_at: datetime.datetime

    currency: Currency = "usd"  # type: ignore[assignment]

    customer_email: Optional[str] = None

    customer_id: Optional[str] = None

    default_payment_method: Optional[str] = None

    description: Optional[str] = None

    discounts: Optional[List[Discount]] = None

    id: Optional[str] = None

    lines: Optional[List[InvoiceLineItem]] = None

    metadata: Dict[str, str] = {}

    number: Optional[str] = None

    paid: bool = False

    pdf: Optional[str] = None

    receipt_number: Optional[str] = None

    statement_descriptor: Optional[str] = None

    status: Optional[InvoiceStatus] = None

    subscription_id: Optional[str] = None

    subtotal: float = 0.0

    tax: float = 0.0

    total: float = 0.0

    url: Optional[str] = None
