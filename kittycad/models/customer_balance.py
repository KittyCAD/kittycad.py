import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.subscription_tier_price import SubscriptionTierPrice
from ..models.uuid import Uuid
from ..models.zoo_product_subscriptions import ZooProductSubscriptions
from .base64data import Base64Data


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
