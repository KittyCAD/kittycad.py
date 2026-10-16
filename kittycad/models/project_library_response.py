import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectLibraryResponse(KittyCadBaseModel):
    """A cloud project library visible to the caller."""

    can_manage: bool

    created_at: datetime.datetime

    id: Uuid

    name: str

    org_id: Optional[Uuid] = None

    revision: str

    updated_at: datetime.datetime

    user_id: Optional[Uuid] = None
