import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class LeafNode(BaseModel):
    """Leaf node information."""
    
    
    auth_timeout: Optional[int] = None
    
    
    
    host: Optional[str] = None
    
    
    
    port: Optional[int] = None
    
    
    
    tls_timeout: Optional[int] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )