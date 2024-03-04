import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data



class KclCodeCompletionParams(BaseModel):
    """Extra params for the completions."""
    
    
    language: Optional[str] = None
    
    
    
    next_indent: Optional[int] = None
    
    
    
    prompt_tokens: Optional[int] = None
    
    
    
    suffix_tokens: Optional[int] = None
    
    
    
    trim_by_indentation: Optional[bool] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )