from typing import Optional

from ..models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)
from .base import KittyCadBaseModel


class ZooProductSubscriptionsUserRequest(KittyCadBaseModel):
    """A struct of Zoo product subscriptions a user can request."""

    modeling_app: ModelingAppIndividualSubscriptionTier = "free"  # type: ignore[assignment]

    pay_annually: Optional[bool] = None
