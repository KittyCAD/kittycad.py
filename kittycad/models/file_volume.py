import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid


from ..models.unit_volume import UnitVolume


from ..models.file_import_format import FileImportFormat


from ..models.api_call_status import ApiCallStatus



class FileVolume(BaseModel):
    """A file volume result."""
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    error: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    output_unit: UnitVolume
    
    
    
    src_format: FileImportFormat
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    
    
    volume: Optional[float] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )