import datetime
from typing import Optional

from ..models.plan_interval import PlanInterval
from ..models.subscription_plan_billing_model import SubscriptionPlanBillingModel
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class SubscriptionPlanPriceRecord(KittyCadBaseModel):
    """Diesel model representing a row in `subscription_plan_prices`."""

    active: bool

    billing_model: SubscriptionPlanBillingModel

    cadence: PlanInterval

    created_at: datetime.datetime

    id: Uuid

    stripe_price_id: Optional[str] = None

    subscription_plan_id: Uuid

    unit_amount: Optional[str] = None

    updated_at: datetime.datetime
