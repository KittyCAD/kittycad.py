from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_token import ApiToken


class ApiTokenResultsPage(BaseModel):
    """A single page of results"""

    items: List[ApiToken]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
