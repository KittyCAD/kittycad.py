from typing import List, Optional

from ..models.invoice import Invoice
from .base import KittyCadBaseModel


class InvoiceResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[Invoice]

    next_page: Optional[str] = None
