from typing import List, Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class UpdateProjectRequest(KittyCadBaseModel):
    """Request payload for replacing a user-owned project."""

    category_ids: Optional[List[Uuid]] = []

    deleted_paths: Optional[List[str]] = None

    description: Optional[str] = ""

    entrypoint_path: Optional[str] = "main.kcl"

    expected_revision: Optional[str] = None

    library_id: Optional[str] = None

    publication_status: Optional[str] = None

    title: str
