from typing import List, Optional

from ..models.factory_customer_catalog_option import FactoryCustomerCatalogOption
from .base import KittyCadBaseModel


class FactoryCustomerCatalogOptionResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[FactoryCustomerCatalogOption]

    next_page: Optional[str] = None
