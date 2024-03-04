import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class CacheMetadata(BaseModel):
    """Metadata about our cache.

This is mostly used for internal purposes and debugging."""
    
    
    ok: bool
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )