from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.payment_method_card_checks import PaymentMethodCardChecks


class CardDetails(BaseModel):
    """The card details of a payment method."""

    brand: Optional[str] = None

    checks: Optional[PaymentMethodCardChecks] = None

    country: Optional[str] = None

    exp_month: Optional[int] = None

    exp_year: Optional[int] = None

    fingerprint: Optional[str] = None

    funding: Optional[str] = None

    last4: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
