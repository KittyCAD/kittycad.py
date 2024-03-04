import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid



class VerificationTokenResponse(BaseModel):
    """A verification token response."""
    
    
    created_at: datetime.datetime
    
    
    
    expires: datetime.datetime
    
    
    
    id: Uuid
    
    
    
    identifier: Optional[str] = None
    
    
    
    saml_redirect_url: Optional[str] = None
    
    
    
    updated_at: datetime.datetime
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )