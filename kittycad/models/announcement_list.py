from typing import List

from ..models.announcement import Announcement
from .base import KittyCadBaseModel


class AnnouncementList(KittyCadBaseModel):
    """Response containing active announcements."""

    announcements: List[Announcement]
