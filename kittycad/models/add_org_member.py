import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.user_org_role import UserOrgRole
from .base64data import Base64Data


class AddOrgMember(BaseModel):
    """Data for adding a member to an org."""

    email: str

    role: UserOrgRole

    model_config = ConfigDict(protected_namespaces=())
