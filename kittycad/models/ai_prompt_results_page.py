import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.ai_prompt import AiPrompt



class AiPromptResultsPage(BaseModel):
    """A single page of results"""
    
    
    items: List[AiPrompt]
    
    
    
    next_page: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )