from typing import List, Optional

from ..models.announcement import Announcement
from .base import KittyCadBaseModel


class AnnouncementResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[Announcement]

    next_page: Optional[str] = None
