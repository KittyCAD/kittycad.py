import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.camera_settings import CameraSettings



class CameraDragEnd(BaseModel):
    """The response from the `CameraDragEnd` command."""
    
    
    settings: CameraSettings
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )