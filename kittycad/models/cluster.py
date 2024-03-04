import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class Cluster(BaseModel):
    """Cluster information."""
    
    
    addr: Optional[str] = None
    
    
    
    auth_timeout: Optional[int] = None
    
    
    
    cluster_port: Optional[int] = None
    
    
    
    name: Optional[str] = None
    
    
    
    tls_timeout: Optional[int] = None
    
    
    
    urls: Optional[List[str]] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )