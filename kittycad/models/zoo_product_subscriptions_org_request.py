from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)


class ZooProductSubscriptionsOrgRequest(BaseModel):
    """A struct of Zoo product subscriptions an organization can request."""

    modeling_app: Optional[ModelingAppOrganizationSubscriptionTier] = None

    model_config = ConfigDict(protected_namespaces=())
