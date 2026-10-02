from typing import List, Optional

from ..models.public_project_response import PublicProjectResponse
from .base import KittyCadBaseModel


class PublicProjectResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[PublicProjectResponse]

    next_page: Optional[str] = None
