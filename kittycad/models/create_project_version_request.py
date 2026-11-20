from typing import List, Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class CreateProjectVersionRequest(KittyCadBaseModel):
    """Request payload for saving a version without changing the current version."""

    deleted_paths: Optional[List[str]] = None

    description: Optional[str] = ""

    entrypoint_path: Optional[str] = "main.kcl"

    parent_version_id: Uuid

    title: str
