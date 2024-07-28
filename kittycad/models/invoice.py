import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.currency import Currency
from ..models.discount import Discount
from ..models.invoice_line_item import InvoiceLineItem
from ..models.invoice_status import InvoiceStatus


class Invoice(BaseModel):
    """An invoice."""

    amount_due: Optional[float] = None

    amount_paid: Optional[float] = None

    amount_remaining: Optional[float] = None

    attempt_count: Optional[int] = None

    attempted: Optional[bool] = None

    created_at: datetime.datetime

    currency: Optional[Currency] = None

    customer_email: Optional[str] = None

    customer_id: Optional[str] = None

    default_payment_method: Optional[str] = None

    description: Optional[str] = None

    discounts: Optional[List[Discount]] = None

    id: Optional[str] = None

    lines: Optional[List[InvoiceLineItem]] = None

    metadata: Optional[Dict[str, str]] = None

    number: Optional[str] = None

    paid: Optional[bool] = None

    pdf: Optional[str] = None

    receipt_number: Optional[str] = None

    statement_descriptor: Optional[str] = None

    status: Optional[InvoiceStatus] = None

    subtotal: Optional[float] = None

    tax: Optional[float] = None

    total: Optional[float] = None

    url: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
