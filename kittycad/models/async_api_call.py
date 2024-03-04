import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid


from ..models.api_call_status import ApiCallStatus


from ..models.async_api_call_type import AsyncApiCallType



class AsyncApiCall(BaseModel):
    """An async API call."""
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    error: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    input: Optional[Any] = None
    
    
    
    output: Optional[Any] = None
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    type: AsyncApiCallType
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    
    
    worker: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )