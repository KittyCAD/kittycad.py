from typing import List, Optional

from ..models.org_skill_response import OrgSkillResponse
from .base import KittyCadBaseModel


class OrgSkillResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[OrgSkillResponse]

    next_page: Optional[str] = None
