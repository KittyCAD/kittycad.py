from typing import List, Optional

from ..models.o_auth2_app_response import OAuth2AppResponse
from .base import KittyCadBaseModel


class OAuth2AppResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[OAuth2AppResponse]

    next_page: Optional[str] = None
