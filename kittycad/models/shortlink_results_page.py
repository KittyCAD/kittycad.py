from typing import List, Optional

from ..models.shortlink import Shortlink
from .base import KittyCadBaseModel


class ShortlinkResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[Shortlink]

    next_page: Optional[str] = None
