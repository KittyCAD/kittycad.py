import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class Shortlink(KittyCadBaseModel):
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
