import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ok_web_socket_response_data import OkWebSocketResponseData



class SuccessWebSocketResponse(BaseModel):
    """Successful Websocket response."""
    
    
    request_id: Optional[str] = None
    
    
    
    resp: OkWebSocketResponseData
    
    
    
    success: bool
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )