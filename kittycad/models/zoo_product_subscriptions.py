import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.modeling_app_subscription_tier import ModelingAppSubscriptionTier



class ZooProductSubscriptions(BaseModel):
    """A struct of Zoo product subscriptions."""
    
    
    modeling_app: ModelingAppSubscriptionTier
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )