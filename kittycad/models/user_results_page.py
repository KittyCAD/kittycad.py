import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.user import User



class UserResultsPage(BaseModel):
    """A single page of results"""
    
    
    items: List[User]
    
    
    
    next_page: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )