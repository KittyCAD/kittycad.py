import datetime
from typing import Dict, List, Optional

from ..models.currency import Currency
from ..models.discount import Discount
from ..models.invoice_line_item import InvoiceLineItem
from ..models.invoice_status import InvoiceStatus
from .base import KittyCadBaseModel


class Invoice(KittyCadBaseModel):
    """An invoice."""

    amount_due: Optional[float] = 0.0

    amount_paid: Optional[float] = 0.0

    amount_remaining: Optional[float] = 0.0

    attempt_count: Optional[int] = 0

    attempted: Optional[bool] = False

    created_at: datetime.datetime

    currency: Optional[Currency] = "usd"  # type: ignore[assignment]

    customer_email: Optional[str] = None

    customer_id: Optional[str] = None

    default_payment_method: Optional[str] = None

    description: Optional[str] = None

    discounts: Optional[List[Discount]] = None

    id: Optional[str] = None

    lines: Optional[List[InvoiceLineItem]] = None

    metadata: Optional[Dict[str, str]] = {}

    number: Optional[str] = None

    paid: Optional[bool] = False

    pdf: Optional[str] = None

    receipt_number: Optional[str] = None

    statement_descriptor: Optional[str] = None

    status: Optional[InvoiceStatus] = None

    subtotal: Optional[float] = 0.0

    tax: Optional[float] = 0.0

    total: Optional[float] = 0.0

    url: Optional[str] = None
