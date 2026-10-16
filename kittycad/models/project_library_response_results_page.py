from typing import List, Optional

from ..models.project_library_response import ProjectLibraryResponse
from .base import KittyCadBaseModel


class ProjectLibraryResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ProjectLibraryResponse]

    next_page: Optional[str] = None
