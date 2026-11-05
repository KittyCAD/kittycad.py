from typing import List, Optional

from ..models.factory_customer_job_version import FactoryCustomerJobVersion
from .base import KittyCadBaseModel


class FactoryCustomerJobVersionResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[FactoryCustomerJobVersion]

    next_page: Optional[str] = None
