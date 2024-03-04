import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class OAuth2ClientInfo(BaseModel):
    """Information about an OAuth 2.0 client."""
    
    
    csrf_token: Optional[str] = None
    
    
    
    pkce_code_verifier: Optional[str] = None
    
    
    
    url: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )