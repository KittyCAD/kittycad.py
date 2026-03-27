import datetime
from typing import Optional

from ..models.kcl_project_file_role import KclProjectFileRole
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class ProjectFileResponse(KittyCadBaseModel):
    """Owner-visible metadata for one stored project file."""

    byte_size: int

    content_type: str

    created_at: datetime.datetime

    file_role: KclProjectFileRole

    id: Uuid

    relative_path: str

    sha256: Optional[str] = None

    sort_order: int

    updated_at: datetime.datetime
