import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.org_member import OrgMember



class OrgMemberResultsPage(BaseModel):
    """A single page of results"""
    
    
    items: List[OrgMember]
    
    
    
    next_page: Optional[str] = None
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )