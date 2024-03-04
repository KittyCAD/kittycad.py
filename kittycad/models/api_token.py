import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid



class ApiToken(BaseModel):
    """An API token.

These are used to authenticate users with Bearer authentication."""
    
    
    created_at: datetime.datetime
    
    
    
    id: Uuid
    
    
    
    is_valid: bool
    
    
    
    label: Optional[str] = None
    
    
    
    token: Uuid
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )