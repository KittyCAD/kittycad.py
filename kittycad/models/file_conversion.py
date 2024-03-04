import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid


from ..models.file_export_format import FileExportFormat


from ..models.output_format import OutputFormat


from ..models.file_import_format import FileImportFormat


from ..models.input_format import InputFormat


from ..models.api_call_status import ApiCallStatus



class FileConversion(BaseModel):
    """A file conversion."""
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    error: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    output_format: FileExportFormat
    
    
    
    output_format_options: Optional[OutputFormat] = None
    
    
    
    outputs: Optional[Dict[str, Base64Data]] = None
    
    
    
    src_format: FileImportFormat
    
    
    
    src_format_options: Optional[InputFormat] = None
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )