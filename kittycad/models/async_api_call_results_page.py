from typing import List, Optional

from pydantic import BaseModel

from ..models.async_api_call import AsyncApiCall


class AsyncApiCallResultsPage(BaseModel):
    """A single page of results"""

    items: List[AsyncApiCall]

    next_page: Optional[str] = None
