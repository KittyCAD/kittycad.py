import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.unit_angle import UnitAngle



class Angle(BaseModel):
    """An angle, with a specific unit."""
    
    
    unit: UnitAngle
    
    
    
    value: float
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )