import datetime
from typing import Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectPublicationInfoResponse(KittyCadBaseModel):
    """Owner-facing publication metadata for a project."""

    has_unpublished_changes: bool

    last_published_at: Optional[datetime.datetime] = None

    last_published_version_id: Optional[Uuid] = None

    submitted_at: Optional[datetime.datetime] = None
