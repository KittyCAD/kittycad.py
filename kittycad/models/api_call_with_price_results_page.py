from typing import List, Optional

from ..models.api_call_with_price import ApiCallWithPrice
from .base import KittyCadBaseModel


class ApiCallWithPriceResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[ApiCallWithPrice]

    next_page: Optional[str] = None
