from typing import List, Optional

from ..models.service_account import ServiceAccount
from .base import KittyCadBaseModel


class ServiceAccountResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ServiceAccount]

    next_page: Optional[str] = None
