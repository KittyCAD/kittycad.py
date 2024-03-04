import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.point3d import Point3d



class CurveGetEndPoints(BaseModel):
    """Endpoints of a curve"""
    
    
    end: Point3d
    
    
    
    start: Point3d
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )