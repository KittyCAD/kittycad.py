from typing import List, Optional

from ..models.project_version_summary_response import ProjectVersionSummaryResponse
from .base import KittyCadBaseModel


class ProjectVersionSummaryResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ProjectVersionSummaryResponse]

    next_page: Optional[str] = None
