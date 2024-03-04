import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.point3d import Point3d



class CameraSettings(BaseModel):
    """Camera settings including position, center, fov etc"""
    
    
    center: Point3d
    
    
    
    fov_y: Optional[float] = None
    
    
    
    ortho: bool
    
    
    
    ortho_scale: Optional[float] = None
    
    
    
    pos: Point3d
    
    
    
    up: Point3d
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )