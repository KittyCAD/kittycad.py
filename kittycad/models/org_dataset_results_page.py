from typing import List, Optional

from ..models.org_dataset import OrgDataset
from .base import KittyCadBaseModel


class OrgDatasetResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[OrgDataset]

    next_page: Optional[str] = None
