import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.country_code import CountryCode



class AddressDetails(BaseModel):
    """Address details."""
    
    
    city: Optional[str] = None
    
    
    
    country: CountryCode
    
    
    
    state: Optional[str] = None
    
    
    
    street1: Optional[str] = None
    
    
    
    street2: Optional[str] = None
    
    
    
    zip: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )