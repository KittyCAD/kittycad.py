from typing import List, Optional

from ..models.factory_customer_job_summary import FactoryCustomerJobSummary
from .base import KittyCadBaseModel


class FactoryCustomerJobSummaryResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[FactoryCustomerJobSummary]

    next_page: Optional[str] = None
