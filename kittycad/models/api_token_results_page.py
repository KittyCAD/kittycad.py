from typing import List, Optional

from ..models.api_token import ApiToken
from .base import KittyCadBaseModel


class ApiTokenResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ApiToken]

    next_page: Optional[str] = None
