import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class DiscountCode(BaseModel):
    """A discount code for a store."""
    
    
    code: str
    
    
    
    expires_at: Optional[datetime.datetime] = None
    
    
    
    percent_off: int
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )