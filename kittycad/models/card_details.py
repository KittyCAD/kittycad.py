from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.payment_method_card_checks import PaymentMethodCardChecks


class CardDetails(BaseModel):
    """The card details of a payment method."""

    brand: Optional[str] = None

    checks: PaymentMethodCardChecks = {}

    country: Optional[str] = None

    exp_month: int = 0

    exp_year: int = 0

    fingerprint: Optional[str] = None

    funding: Optional[str] = None

    last4: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
