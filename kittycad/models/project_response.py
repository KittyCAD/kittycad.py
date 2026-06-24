import datetime
from typing import List, Optional

from ..models.kcl_project_preview_status import KclProjectPreviewStatus
from ..models.kcl_project_publication_status import KclProjectPublicationStatus
from ..models.project_file_response import ProjectFileResponse
from ..models.project_publication_info_response import ProjectPublicationInfoResponse
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

    preview_url: Optional[str] = None

    project_toml_path: str

    publication: ProjectPublicationInfoResponse

    publication_status: KclProjectPublicationStatus

    revision: str

    title: str

    updated_at: datetime.datetime
