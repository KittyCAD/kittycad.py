from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.shortlink import Shortlink


class ShortlinkResultsPage(BaseModel):
    """A single page of results"""

    items: List[Shortlink]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
