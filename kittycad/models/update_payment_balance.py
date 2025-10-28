from typing import Optional

from .base import KittyCadBaseModel


class UpdatePaymentBalance(KittyCadBaseModel):
    """Payload for updating a user's balance."""

    monthly_api_credits_remaining_monetary_value: Optional[float] = None

    stable_api_credits_remaining_monetary_value: Optional[float] = None
