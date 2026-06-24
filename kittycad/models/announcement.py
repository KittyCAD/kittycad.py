import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class Announcement(KittyCadBaseModel):
    """An announcement broadcast to all clients."""

    active: bool

    body: Optional[str] = None

    created_at: datetime.datetime

    id: Uuid

    tag: Optional[str] = None

    title: str

    updated_at: datetime.datetime
