import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.point3d import Point3d


from ..models.uuid import Uuid


from ..models.unit_length import UnitLength


from ..models.file_import_format import FileImportFormat


from ..models.api_call_status import ApiCallStatus



class FileCenterOfMass(BaseModel):
    """A file center of mass result."""
    
    
    center_of_mass: Optional[Point3d] = None
    
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    error: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    output_unit: UnitLength
    
    
    
    src_format: FileImportFormat
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )