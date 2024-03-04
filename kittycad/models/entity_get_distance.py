import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.length_unit import LengthUnit



class EntityGetDistance(BaseModel):
    """The response from the `EntitiesGetDistance` command."""
    
    
    max_distance: LengthUnit
    
    
    
    min_distance: LengthUnit
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )