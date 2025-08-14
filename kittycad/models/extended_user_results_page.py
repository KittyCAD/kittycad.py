from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.extended_user import ExtendedUser


class ExtendedUserResultsPage(BaseModel):
    """A single page of results"""

    items: List[ExtendedUser]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
