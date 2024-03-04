import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.block_reason import BlockReason
from ..models.uuid import Uuid


class User(BaseModel):
    """A user."""

    block: Optional[BlockReason] = None

    can_train_on_data: Optional[bool] = None

    company: Optional[str] = None

    created_at: datetime.datetime

    discord: Optional[str] = None

    email: Optional[str] = None

    email_verified: Optional[datetime.datetime] = None

    first_name: Optional[str] = None

    github: Optional[str] = None

    id: Uuid

    image: str

    is_service_account: Optional[bool] = None

    last_name: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
