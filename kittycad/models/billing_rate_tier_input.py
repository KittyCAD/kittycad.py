from typing import Optional

from ..models.billing_quantity import BillingQuantity
from .base import KittyCadBaseModel


class BillingRateTierInput(KittyCadBaseModel):
    """Serialized rate tier payload for a usage-rated contract item."""

    tier_end_exclusive: Optional[BillingQuantity] = None

    tier_start_inclusive: BillingQuantity

    unit_price: float
