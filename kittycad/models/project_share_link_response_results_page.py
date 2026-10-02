from typing import List, Optional

from ..models.project_share_link_response import ProjectShareLinkResponse
from .base import KittyCadBaseModel


class ProjectShareLinkResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ProjectShareLinkResponse]

    next_page: Optional[str] = None
