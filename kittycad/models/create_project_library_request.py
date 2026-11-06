from typing import Optional

from ..models.kcl_project_library_source import KclProjectLibrarySource
from ..models.project_library_scope import ProjectLibraryScope
from .base import KittyCadBaseModel


class CreateProjectLibraryRequest(KittyCadBaseModel):
    """Request to create a cloud project library."""

    name: str

    scope: ProjectLibraryScope

    source: Optional[KclProjectLibrarySource] = "zds"  # type: ignore[assignment]
