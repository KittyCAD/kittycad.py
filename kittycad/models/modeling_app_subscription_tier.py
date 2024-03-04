from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.modeling_app_subscription_tier_name import ModelingAppSubscriptionTierName
from ..models.subscription_tier_feature import SubscriptionTierFeature
from ..models.subscription_tier_price import SubscriptionTierPrice
from ..models.subscription_tier_type import SubscriptionTierType
from ..models.subscription_training_data_behavior import (
    SubscriptionTrainingDataBehavior,
)
from ..models.support_tier import SupportTier
from ..models.zoo_tool import ZooTool


class ModelingAppSubscriptionTier(BaseModel):
    """A subscription tier we offer for the Modeling App."""

    description: str

    features: Optional[List[SubscriptionTierFeature]] = None

    name: ModelingAppSubscriptionTierName

    pay_as_you_go_credits: float

    price: SubscriptionTierPrice

    support_tier: SupportTier

    training_data_behavior: SubscriptionTrainingDataBehavior

    type: SubscriptionTierType

    zoo_tools_included: Optional[List[ZooTool]] = None

    model_config = ConfigDict(protected_namespaces=())
