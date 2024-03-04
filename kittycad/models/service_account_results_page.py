from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.service_account import ServiceAccount


class ServiceAccountResultsPage(BaseModel):
    """A single page of results"""

    items: List[ServiceAccount]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
