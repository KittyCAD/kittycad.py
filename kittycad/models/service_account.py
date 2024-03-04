import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid



class ServiceAccount(BaseModel):
    """A service account.

These are used to authenticate orgs with Bearer authentication.

This works just like an API token, but it is tied to an organization versus an individual user."""
    
    
    created_at: datetime.datetime
    
    
    
    id: Uuid
    
    
    
    is_valid: bool
    
    
    
    label: Optional[str] = None
    
    
    
    org_id: Uuid
    
    
    
    token: Uuid
    
    
    
    updated_at: datetime.datetime
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )