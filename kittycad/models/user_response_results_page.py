from typing import List, Optional

from ..models.user_response import UserResponse
from .base import KittyCadBaseModel


class UserResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[UserResponse]

    next_page: Optional[str] = None
