import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class PerspectiveCameraParameters(BaseModel):
    """Defines a perspective view."""
    
    
    fov_y: float
    
    
    
    z_far: float
    
    
    
    z_near: float
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )