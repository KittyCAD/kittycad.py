import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.annotation_text_alignment_x import AnnotationTextAlignmentX


from ..models.annotation_text_alignment_y import AnnotationTextAlignmentY



class AnnotationTextOptions(BaseModel):
    """Options for annotation text"""
    
    
    point_size: int
    
    
    
    text: str
    
    
    
    x: AnnotationTextAlignmentX
    
    
    
    y: AnnotationTextAlignmentY
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )