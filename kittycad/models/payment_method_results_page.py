from typing import List, Optional

from ..models.payment_method import PaymentMethod
from .base import KittyCadBaseModel


class PaymentMethodResultsPage(KittyCadBaseModel):
    """A single page of results"""

    items: List[PaymentMethod]

    next_page: Optional[str] = None
