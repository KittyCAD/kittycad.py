import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.org_role import OrgRole
from ..models.uuid import Uuid
from .base64data import Base64Data


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

    model_config = ConfigDict(protected_namespaces=())
