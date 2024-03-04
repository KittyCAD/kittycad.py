import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class ClientMetrics(BaseModel):
    """ClientMetrics contains information regarding the state of the peer."""
    
    
    rtc_frames_decoded: int
    
    
    
    rtc_frames_dropped: int
    
    
    
    rtc_frames_per_second: int
    
    
    
    rtc_frames_received: int
    
    
    
    rtc_freeze_count: int
    
    
    
    rtc_jitter_sec: float
    
    
    
    rtc_keyframes_decoded: int
    
    
    
    rtc_total_freezes_duration_sec: float
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )