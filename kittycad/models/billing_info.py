import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.address_details import AddressDetails



class BillingInfo(BaseModel):
    """The billing information for payments."""
    
    
    address: Optional[AddressDetails] = None
    
    
    
    name: Optional[str] = None
    
    
    
    phone: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )