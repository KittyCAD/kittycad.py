from typing import List, Optional

from ..models.payment_method import PaymentMethod
from .base import KittyCadBaseModel


class PaymentMethodResultsPage(KittyCadBaseModel):
    """A single page of payment methods and the default selected for this traversal."""

    default_payment_method_id: Optional[str] = None

    items: List[PaymentMethod]

    next_page: Optional[str] = None
