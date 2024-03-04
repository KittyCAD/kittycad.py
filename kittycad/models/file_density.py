import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid


from ..models.unit_mass import UnitMass


from ..models.unit_density import UnitDensity


from ..models.file_import_format import FileImportFormat


from ..models.api_call_status import ApiCallStatus



class FileDensity(BaseModel):
    """A file density result."""
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    density: Optional[float] = None
    
    
    
    error: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    material_mass: Optional[float] = None
    
    
    
    material_mass_unit: UnitMass
    
    
    
    output_unit: UnitDensity
    
    
    
    src_format: FileImportFormat
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )