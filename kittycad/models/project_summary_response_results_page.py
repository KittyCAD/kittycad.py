from typing import List, Optional

from ..models.project_summary_response import ProjectSummaryResponse
from .base import KittyCadBaseModel


class ProjectSummaryResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ProjectSummaryResponse]

    next_page: Optional[str] = None
