from typing import List, Optional

from ..models.org_member import OrgMember
from .base import KittyCadBaseModel


class OrgMemberResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[OrgMember]

    next_page: Optional[str] = None
