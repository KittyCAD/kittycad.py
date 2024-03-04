import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.length_unit import LengthUnit



class Point2d(BaseModel):
    """A point in 2D space"""
    
    
    x: LengthUnit
    
    
    
    y: LengthUnit
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )