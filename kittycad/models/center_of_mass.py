import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.point3d import Point3d


from ..models.unit_length import UnitLength



class CenterOfMass(BaseModel):
    """The center of mass response."""
    
    
    center_of_mass: Point3d
    
    
    
    output_unit: UnitLength
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )