import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class OrgDetails(BaseModel):
    """The user-modifiable parts of an organization."""
    
    
    allow_users_in_domain_to_auto_join: Optional[bool] = None
    
    
    
    billing_email: Optional[str] = None
    
    
    
    domain: Optional[str] = None
    
    
    
    image: Optional[str] = None
    
    
    
    name: Optional[str] = None
    
    
    
    phone: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )