from typing import List, Optional

from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class CreateProjectRequest(KittyCadBaseModel):
    """Request payload for creating or replacing a user-owned project."""

    category_ids: Optional[List[Uuid]] = []

    description: Optional[str] = ""

    entrypoint_path: Optional[str] = "main.kcl"

    library_id: Optional[str] = None

    publication_status: Optional[str] = None

    title: str
