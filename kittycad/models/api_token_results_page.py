from typing import List, Optional

from pydantic import BaseModel

from ..models.api_token import ApiToken


class ApiTokenResultsPage(BaseModel):
    """A single page of results"""

    items: List[ApiToken]

    next_page: Optional[str] = None
