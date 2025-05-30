from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.modeling_app_individual_subscription_tier import (
    ModelingAppIndividualSubscriptionTier,
)


class ZooProductSubscriptionsUserRequest(BaseModel):
    """A struct of Zoo product subscriptions a user can request."""

    modeling_app: ModelingAppIndividualSubscriptionTier = "free"  # type: ignore

    pay_annually: Optional[bool] = None

    model_config = ConfigDict(protected_namespaces=())
