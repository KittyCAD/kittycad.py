import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.o_auth2_grant_type import OAuth2GrantType



class DeviceAccessTokenRequestForm(BaseModel):
    """The form for a device access token request."""
    
    
    client_id: str
    
    
    
    device_code: str
    
    
    
    grant_type: OAuth2GrantType
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )