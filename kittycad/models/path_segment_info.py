import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.path_command import PathCommand


from ..models.modeling_cmd_id import ModelingCmdId



class PathSegmentInfo(BaseModel):
    """Info about a path segment"""
    
    
    command: PathCommand
    
    
    
    command_id: Optional[ModelingCmdId] = None
    
    
    
    relative: bool
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )