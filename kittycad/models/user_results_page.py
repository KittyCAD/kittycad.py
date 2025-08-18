from typing import List, Optional

from ..models.user import User
from .base import KittyCadBaseModel


class UserResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[User]

    next_page: Optional[str] = None
