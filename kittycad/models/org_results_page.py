from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.org import Org


class OrgResultsPage(BaseModel):
    """A single page of results"""

    items: List[Org]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
