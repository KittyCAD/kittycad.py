from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_endpoint import ApiEndpoint
from ..models.modeling_app_share_links import ModelingAppShareLinks
from ..models.modeling_app_subscription_tier_name import ModelingAppSubscriptionTierName
from ..models.subscription_tier_feature import SubscriptionTierFeature
from ..models.subscription_tier_price import SubscriptionTierPrice
from ..models.subscription_tier_type import SubscriptionTierType
from ..models.subscription_training_data_behavior import (
    SubscriptionTrainingDataBehavior,
)
from ..models.support_tier import SupportTier
from ..models.zoo_tool import ZooTool


class ZooProductSubscription(BaseModel):
    """A subscription to the modeling app."""

    annual_discount: Optional[int] = None

    description: str

    endpoints_included: Optional[List[ApiEndpoint]] = None

    features: Optional[List[SubscriptionTierFeature]] = None

    monthly_pay_as_you_go_api_credits: int = 0

    monthly_pay_as_you_go_api_credits_monetary_value: float

    name: ModelingAppSubscriptionTierName

    pay_as_you_go_api_credit_price: float = 0.0

    price: SubscriptionTierPrice

    share_links: Optional[List[ModelingAppShareLinks]] = None

    support_tier: SupportTier

    training_data_behavior: SubscriptionTrainingDataBehavior

    type: SubscriptionTierType

    zoo_tools_included: Optional[List[ZooTool]] = None

    model_config = ConfigDict(protected_namespaces=())
