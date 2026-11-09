from ..models.currency import Currency
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class FactoryQuotePreview(KittyCadBaseModel):
    """Current checkout amounts in USD cents, before accepting or collecting payment."""

    account_balance_adjustment_cents: int

    amount_due_cents: int

    available_credits_cents: int

    credits_applied_cents: int

    currency: Currency

    quote_id: Uuid

    shipping_cents: int

    subtotal_cents: int

    tax_cents: int

    total_cents: int
