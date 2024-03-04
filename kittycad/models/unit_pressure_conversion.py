import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid


from ..models.unit_pressure import UnitPressure


from ..models.api_call_status import ApiCallStatus



class UnitPressureConversion(BaseModel):
    """Result of converting between units."""
    
    
    completed_at: Optional[datetime.datetime] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    error: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    input: Optional[float] = None
    
    
    
    input_unit: UnitPressure
    
    
    
    output: Optional[float] = None
    
    
    
    output_unit: UnitPressure
    
    
    
    started_at: Optional[datetime.datetime] = None
    
    
    
    status: ApiCallStatus
    
    
    
    updated_at: datetime.datetime
    
    
    
    user_id: Uuid
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )