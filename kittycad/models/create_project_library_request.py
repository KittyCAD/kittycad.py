from ..models.project_library_scope import ProjectLibraryScope
from .base import KittyCadBaseModel


class CreateProjectLibraryRequest(KittyCadBaseModel):
    """Request to create a cloud project library."""

    name: str

    scope: ProjectLibraryScope
