from typing import Optional

from .base import KittyCadBaseModel


class UpdateProjectLibraryRequest(KittyCadBaseModel):
    """Request payload for moving a project to a library or leaving it unassigned."""

    expected_revision: str

    library_id: Optional[str] = None
