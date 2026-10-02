import datetime
from typing import Optional

from ..models.kcl_project_preview_status import KclProjectPreviewStatus
from ..models.kcl_project_version_ancestry_status import KclProjectVersionAncestryStatus
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectVersionSummaryResponse(KittyCadBaseModel):
    """A saved version in a project's history."""

    ancestry_status: KclProjectVersionAncestryStatus

    created_at: datetime.datetime

    id: Uuid

    is_current: bool

    parent_version_id: Optional[Uuid] = None

    preview_status: KclProjectPreviewStatus

    title: str
