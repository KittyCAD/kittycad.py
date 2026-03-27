import datetime
from typing import List, Optional

from ..models.kcl_project_preview_status import KclProjectPreviewStatus
from ..models.kcl_project_publication_status import KclProjectPublicationStatus
from ..models.project_file_response import ProjectFileResponse
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectResponse(KittyCadBaseModel):
    """Owner-visible project detail payload."""

    category_ids: List[Uuid]

    created_at: datetime.datetime

    description: str

    entrypoint_path: str

    files: List[ProjectFileResponse]

    id: Uuid

    preview_status: KclProjectPreviewStatus

    primary_preview_height: Optional[int] = None

    primary_preview_path: Optional[str] = None

    primary_preview_version: Optional[str] = None

    primary_preview_width: Optional[int] = None

    project_toml_path: str

    publication_status: KclProjectPublicationStatus

    title: str

    updated_at: datetime.datetime
