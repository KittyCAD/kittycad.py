import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.uuid import Uuid


class Shortlink(BaseModel):
    """A short url."""

    created_at: datetime.datetime

    id: Uuid

    key: str

    org_id: Optional[Uuid] = None

    password_hash: Optional[str] = None

    restrict_to_org: bool = False

    updated_at: datetime.datetime

    user_id: Uuid

    value: str

    model_config = ConfigDict(protected_namespaces=())
