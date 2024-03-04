import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class MouseClick(BaseModel):
    """The response from the `MouseClick` command."""
    
    
    entities_modified: List[str]
    
    
    
    entities_selected: List[str]
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )