import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.cache_metadata import CacheMetadata


from ..models.environment import Environment


from ..models.file_system_metadata import FileSystemMetadata


from ..models.connection import Connection



class Metadata(BaseModel):
    """Metadata about our currently running server.

This is mostly used for internal purposes and debugging."""
    
    
    cache: CacheMetadata
    
    
    
    environment: Environment
    
    
    
    fs: FileSystemMetadata
    
    
    
    git_hash: str
    
    
    
    pubsub: Connection
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )