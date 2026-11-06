from typing import List, Optional

from ..models.address_response import AddressResponse
from .base import KittyCadBaseModel


class AddressResponseResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[AddressResponse]

    next_page: Optional[str] = None
