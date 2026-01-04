from ..models.plan_interval import PlanInterval
from ..models.subscription_plan_billing_model import SubscriptionPlanBillingModel
from .base import KittyCadBaseModel


class PriceUpsertRequest(KittyCadBaseModel):
    """Create or update a price row for a subscription plan."""

    active: bool = True

    billing_model: SubscriptionPlanBillingModel

    cadence: PlanInterval

    unit_amount: float
