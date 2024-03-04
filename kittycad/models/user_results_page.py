from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.user import User


class UserResultsPage(BaseModel):
    """A single page of results"""

    items: List[User]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
