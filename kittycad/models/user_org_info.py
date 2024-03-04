import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.block_reason import BlockReason
from ..models.org_role import OrgRole
from ..models.uuid import Uuid


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

    model_config = ConfigDict(protected_namespaces=())
