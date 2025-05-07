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

    monthly_api_credits_remaining: int

    monthly_api_credits_remaining_monetary_value: float

    stable_api_credits_remaining: int

    stable_api_credits_remaining_monetary_value: float

    subscription_details: Optional[ZooProductSubscriptions] = None

    subscription_id: Optional[str] = None

    total_due: Optional[float] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
