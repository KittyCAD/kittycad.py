import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.block_reason import BlockReason
from ..models.uuid import Uuid


class Org(BaseModel):
    """An organization."""

    allow_users_in_domain_to_auto_join: Optional[bool] = None

    billing_email: str

    billing_email_verified: Optional[datetime.datetime] = None

    block: Optional[BlockReason] = None

    can_train_on_data: bool = False

    created_at: datetime.datetime

    domain: Optional[str] = None

    id: Uuid

    image: Optional[str] = None

    name: Optional[str] = None

    phone: str = ""

    stripe_id: Optional[str] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
