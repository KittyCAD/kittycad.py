import datetime
from typing import List, Optional, Dict, Union, Any, Literal
from uuid import UUID

from pydantic import BaseModel, Base64Bytes, AnyUrl, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber
from .base64data import Base64Data


from ..models.user_org_role import UserOrgRole



class UpdateMemberToOrgBody(BaseModel):
    """Data for updating a member of an org."""
    
    
    role: UserOrgRole
    
    

    model_config = ConfigDict(
        protected_namespaces=()
    )