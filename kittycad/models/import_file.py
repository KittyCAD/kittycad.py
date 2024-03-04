import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class ImportFile(BaseModel):
    """File to import into the current model. If you are sending binary data for a file, be sure to send the WebSocketRequest as binary/bson, not text/json."""
    
    
    data: bytes
    
    
    
    path: str
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )