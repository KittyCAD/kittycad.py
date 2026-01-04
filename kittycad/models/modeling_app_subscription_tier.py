from typing import List, Optional

from ..models.api_endpoint import ApiEndpoint
from ..models.modeling_app_share_links import ModelingAppShareLinks
from ..models.subscription_tier_feature import SubscriptionTierFeature
from ..models.subscription_tier_price import SubscriptionTierPrice
from ..models.subscription_tier_type import SubscriptionTierType
from ..models.subscription_training_data_behavior import (
    SubscriptionTrainingDataBehavior,
)
from ..models.support_tier import SupportTier
from ..models.zoo_tool import ZooTool
from .base import KittyCadBaseModel


class ModelingAppSubscriptionTier(KittyCadBaseModel):
    """Rich information about a Modeling App subscription tier."""

    annual_discount: Optional[float] = None

    description: str

    display_name: str = ""

    endpoints_included: Optional[List[ApiEndpoint]] = None

    features: Optional[List[SubscriptionTierFeature]] = None

    is_custom_quote: bool = False

    ml_custom_models: bool = False

    monthly_pay_as_you_go_api_credits: int = 0

    monthly_pay_as_you_go_api_credits_monetary_value: float = 0.0

    name: str

    pay_as_you_go_api_credit_price: float = 0.0

    price: SubscriptionTierPrice

    share_links: Optional[List[ModelingAppShareLinks]] = None

    support_tier: SupportTier

    training_data_behavior: SubscriptionTrainingDataBehavior

    type: SubscriptionTierType

    zoo_tools_included: Optional[List[ZooTool]] = None
