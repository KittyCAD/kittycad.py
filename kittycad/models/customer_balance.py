import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.subscription_tier_price import SubscriptionTierPrice
from ..models.uuid import Uuid
from ..models.zoo_product_subscriptions import ZooProductSubscriptions


class CustomerBalance(BaseModel):
    """A balance for a customer.

    This holds information about the financial balance for the customer."""

    created_at: datetime.datetime

    id: Uuid

    map_id: Uuid

    modeling_app_enterprise_price: Optional[SubscriptionTierPrice] = None

    monthly_credits_remaining: float

    pre_pay_cash_remaining: float

    pre_pay_credits_remaining: float

    subscription_details: Optional[ZooProductSubscriptions] = None

    subscription_id: Optional[str] = None

    total_due: float

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
