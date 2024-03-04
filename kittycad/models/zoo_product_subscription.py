import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.subscription_tier_feature import SubscriptionTierFeature


from ..models.modeling_app_subscription_tier_name import ModelingAppSubscriptionTierName


from ..models.subscription_tier_price import SubscriptionTierPrice


from ..models.support_tier import SupportTier


from ..models.subscription_training_data_behavior import SubscriptionTrainingDataBehavior


from ..models.subscription_tier_type import SubscriptionTierType


from ..models.zoo_tool import ZooTool



class ZooProductSubscription0(BaseModel):
    """A subscription to the modeling app."""
    
    
    description: str
    
    
    
    features: Optional[List[SubscriptionTierFeature]] = None
    
    
    
    name: ModelingAppSubscriptionTierName
    
    
    
    pay_as_you_go_credits: float
    
    
    
    price: SubscriptionTierPrice
    
    
    
    support_tier: SupportTier
    
    
    
    training_data_behavior: SubscriptionTrainingDataBehavior
    
    
    
    type: SubscriptionTierType
    
    
    
    zoo_tools_included: Optional[List[ZooTool]] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )
from typing import Dict, Any, Union, Type, TypeVar
from pydantic import RootModel, Field

from typing_extensions import Annotated




ZooProductSubscription = RootModel[Union[
        
        ZooProductSubscription0,
        
    ]]

