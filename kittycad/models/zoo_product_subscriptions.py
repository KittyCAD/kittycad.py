from ..models.modeling_app_subscription_tier import ModelingAppSubscriptionTier
from .base import KittyCadBaseModel


class ZooProductSubscriptions(KittyCadBaseModel):
    """A struct of Zoo product subscriptions."""

    modeling_app: ModelingAppSubscriptionTier
