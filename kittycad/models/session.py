import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid



class Session(BaseModel):
    """An authentication session."""
    
    
    created_at: datetime.datetime
    
    
    
    expires: datetime.datetime
    
    
    
    id: Uuid
    
    
    
    session_token: Uuid
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )