import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ai_feedback import AiFeedback


from ..models.uuid import Uuid


from ..models.file_export_format import FileExportFormat


from ..models.api_call_status import ApiCallStatus



class TextToCad(BaseModel):
    """A response from a text to CAD prompt."""
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    error: Optional[str] = None
    
    
    
    feedback: Optional[AiFeedback] = None
    
    
    
    id: Uuid
    
    
    
    model_version: str
    
    
    
    output_format: FileExportFormat
    
    
    
    outputs: Optional[Dict[str, Base64Data]] = None
    
    
    
    prompt: str
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )