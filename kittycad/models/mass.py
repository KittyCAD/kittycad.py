import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.unit_mass import UnitMass



class Mass(BaseModel):
    """The mass response."""
    
    
    mass: float
    
    
    
    output_unit: UnitMass
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )