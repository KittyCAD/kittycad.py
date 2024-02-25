
from pydantic import BaseModel, ConfigDict

from ..models.modeling_app_subscription_tier import ModelingAppSubscriptionTier


class ZooProductSubscriptions(BaseModel):
    """A struct of Zoo product subscriptions."""

    modeling_app: ModelingAppSubscriptionTier

    model_config = ConfigDict(protected_namespaces=())
