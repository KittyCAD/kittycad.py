import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.rtc_sdp_type import RtcSdpType



class RtcSessionDescription(BaseModel):
    """SessionDescription is used to expose local and remote session descriptions."""
    
    
    sdp: str
    
    
    
    type: RtcSdpType
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )