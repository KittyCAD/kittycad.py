from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_call_with_price import ApiCallWithPrice


class ApiCallWithPriceResultsPage(BaseModel):
    """A single page of results"""

    items: List[ApiCallWithPrice]

    next_page: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
