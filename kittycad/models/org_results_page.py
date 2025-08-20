from typing import List, Optional

from ..models.org import Org
from .base import KittyCadBaseModel


class OrgResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[Org]

    next_page: Optional[str] = None
