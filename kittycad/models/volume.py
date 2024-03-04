import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.unit_volume import UnitVolume



class Volume(BaseModel):
    """The volume response."""
    
    
    output_unit: UnitVolume
    
    
    
    volume: float
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )