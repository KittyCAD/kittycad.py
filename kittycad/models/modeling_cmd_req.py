import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.modeling_cmd import ModelingCmd


from ..models.modeling_cmd_id import ModelingCmdId



class ModelingCmdReq(BaseModel):
    """A graphics command submitted to the KittyCAD engine via the Modeling API."""
    
    
    cmd: ModelingCmd
    
    
    
    cmd_id: ModelingCmdId
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )