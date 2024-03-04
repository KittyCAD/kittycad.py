import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.uuid import Uuid


from ..models.org_role import OrgRole



class OrgMember(BaseModel):
    """A member of an organization."""
    
    
    company: Optional[str] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    discord: Optional[str] = None
    
    
    
    email: Optional[str] = None
    
    
    
    email_verified: Optional[datetime.datetime] = None
    
    
    
    first_name: Optional[str] = None
    
    
    
    github: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    image: str
    
    
    
    last_name: Optional[str] = None
    
    
    
    name: Optional[str] = None
    
    
    
    phone: Optional[str] = None
    
    
    
    role: OrgRole
    
    
    
    updated_at: datetime.datetime
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )