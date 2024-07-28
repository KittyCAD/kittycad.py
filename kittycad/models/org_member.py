import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.org_role import OrgRole
from ..models.uuid import Uuid


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
