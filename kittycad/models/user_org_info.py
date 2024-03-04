import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.block_reason import BlockReason


from ..models.uuid import Uuid


from ..models.org_role import OrgRole



class UserOrgInfo(BaseModel):
    """A user's information about an org, including their role."""
    
    
    allow_users_in_domain_to_auto_join: Optional[bool] = None
    
    
    
    billing_email: Optional[str] = None
    
    
    
    billing_email_verified: Optional[datetime.datetime] = None
    
    
    
    block: Optional[BlockReason] = None
    
    
    
    created_at: datetime.datetime
    
    
    
    domain: Optional[str] = None
    
    
    
    id: Uuid
    
    
    
    image: Optional[str] = None
    
    
    
    name: Optional[str] = None
    
    
    
    phone: Optional[str] = None
    
    
    
    role: OrgRole
    
    
    
    stripe_id: Optional[str] = None
    
    
    
    updated_at: datetime.datetime
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )