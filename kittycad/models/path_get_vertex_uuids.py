import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class PathGetVertexUuids(BaseModel):
    """The response from the `PathGetVertexUuids` command."""
    
    
    vertex_ids: List[str]
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )