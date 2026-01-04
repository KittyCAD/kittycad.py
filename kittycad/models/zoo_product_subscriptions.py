from typing import Optional

from ..models.modeling_app_subscription_tier import ModelingAppSubscriptionTier
from ..models.subscription_action_type import SubscriptionActionType
from .base import KittyCadBaseModel


class ZooProductSubscriptions(KittyCadBaseModel):
    """A struct of Zoo product subscriptions."""

    action_client_secret: Optional[str] = None

    action_type: Optional[SubscriptionActionType] = None

    modeling_app: ModelingAppSubscriptionTier
