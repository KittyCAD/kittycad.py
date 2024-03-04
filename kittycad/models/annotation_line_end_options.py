import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.annotation_line_end import AnnotationLineEnd



class AnnotationLineEndOptions(BaseModel):
    """Options for annotation text"""
    
    
    end: AnnotationLineEnd
    
    
    
    start: AnnotationLineEnd
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )