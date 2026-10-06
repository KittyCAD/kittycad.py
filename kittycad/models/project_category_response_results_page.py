from typing import List, Optional

from ..models.project_category_response import ProjectCategoryResponse
from .base import KittyCadBaseModel


class ProjectCategoryResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ProjectCategoryResponse]

    next_page: Optional[str] = None
