from typing import Optional

from ..models.modeling_app_organization_subscription_tier import (
    ModelingAppOrganizationSubscriptionTier,
)
from .base import KittyCadBaseModel


class ZooProductSubscriptionsOrgRequest(KittyCadBaseModel):
    """A struct of Zoo product subscriptions an organization can request."""

    modeling_app: ModelingAppOrganizationSubscriptionTier = "team"  # type: ignore[assignment]

    pay_annually: Optional[bool] = None
