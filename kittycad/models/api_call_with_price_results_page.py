import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.api_call_with_price import ApiCallWithPrice



class ApiCallWithPriceResultsPage(BaseModel):
    """A single page of results"""
    
    
    items: List[ApiCallWithPrice]
    
    
    
    next_page: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )