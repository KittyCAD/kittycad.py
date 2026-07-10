from typing import Optional

from ..models.zoo_product_subscription_downgrade_reason import (
    ZooProductSubscriptionDowngradeReason,
)
from .base import KittyCadBaseModel


class ZooProductSubscriptionsUserRequest(KittyCadBaseModel):
    """A struct of Zoo product subscriptions a user can request."""

    downgrade_reason: Optional[ZooProductSubscriptionDowngradeReason] = None

    downgrade_reason_text: Optional[str] = None

    modeling_app: str

    pay_annually: Optional[bool] = None
