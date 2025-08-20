from typing import List, Optional

from ..models.async_api_call import AsyncApiCall
from .base import KittyCadBaseModel


class AsyncApiCallResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[AsyncApiCall]

    next_page: Optional[str] = None
