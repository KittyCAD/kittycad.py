from typing import Optional

from ..models.payment_method_card_checks import PaymentMethodCardChecks
from .base import KittyCadBaseModel


class CardDetails(KittyCadBaseModel):
    """The card details of a payment method."""

    brand: Optional[str] = None

    checks: PaymentMethodCardChecks = {}  # type: ignore[assignment]

    country: Optional[str] = None

    exp_month: int = 0

    exp_year: int = 0

    fingerprint: Optional[str] = None

    funding: Optional[str] = None

    last4: Optional[str] = None
