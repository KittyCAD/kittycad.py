import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.modeling_app_organization_subscription_tier import ModelingAppOrganizationSubscriptionTier



class ZooProductSubscriptionsOrgRequest(BaseModel):
    """A struct of Zoo product subscriptions an organization can request."""
    
    
    modeling_app: Optional[ModelingAppOrganizationSubscriptionTier] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )