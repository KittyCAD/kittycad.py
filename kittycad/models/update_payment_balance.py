from typing import Optional

from .base import KittyCadBaseModel


class UpdatePaymentBalance(KittyCadBaseModel):
    """The data for updating a balance."""

    monthly_api_credits_remaining_monetary_value: Optional[float] = None

    stable_api_credits_remaining_monetary_value: Optional[float] = None
