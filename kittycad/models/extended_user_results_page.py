from typing import List, Optional

from ..models.extended_user import ExtendedUser
from .base import KittyCadBaseModel


class ExtendedUserResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ExtendedUser]

    next_page: Optional[str] = None
