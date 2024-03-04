import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.async_api_call import AsyncApiCall



class AsyncApiCallResultsPage(BaseModel):
    """A single page of results"""
    
    
    items: List[AsyncApiCall]
    
    
    
    next_page: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )