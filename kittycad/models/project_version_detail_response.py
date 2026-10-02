import datetime
from typing import List, Optional

from ..models.kcl_project_preview_status import KclProjectPreviewStatus
from ..models.kcl_project_version_ancestry_status import KclProjectVersionAncestryStatus
from ..models.project_file_response import ProjectFileResponse
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectVersionDetailResponse(KittyCadBaseModel):
    """Metadata and files for one saved project version."""

    ancestry_status: KclProjectVersionAncestryStatus

    created_at: datetime.datetime

    description: str

    entrypoint_path: str

    files: List[ProjectFileResponse]

    id: Uuid

    is_current: bool

    parent_version_id: Optional[Uuid] = None

    preview_status: KclProjectPreviewStatus

    preview_url: Optional[str] = None

    project_toml_path: str

    title: str
