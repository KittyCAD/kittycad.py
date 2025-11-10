from typing import List, Optional

from ..models.org_dataset_file_conversion_summary import OrgDatasetFileConversionSummary
from .base import KittyCadBaseModel


class OrgDatasetFileConversionSummaryResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[OrgDatasetFileConversionSummary]

    next_page: Optional[str] = None
