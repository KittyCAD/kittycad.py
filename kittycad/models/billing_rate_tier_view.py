from typing import Optional

from ..models.billing_quantity import BillingQuantity
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class BillingRateTierView(KittyCadBaseModel):
    """Serialized rate tier returned from a stored contract."""

    id: Uuid

    tier_end_exclusive: Optional[BillingQuantity] = None

    tier_start_inclusive: BillingQuantity

    unit_price: float
