import datetime
from typing import Dict, Optional

from ..models.billing_info import BillingInfo
from ..models.card_details import CardDetails
from ..models.payment_method_type import PaymentMethodType
from .base import KittyCadBaseModel


class PaymentMethod(KittyCadBaseModel):
    """A payment method."""

    billing_info: BillingInfo

    card: Optional[CardDetails] = None

    created_at: datetime.datetime

    id: Optional[str] = None

    metadata: Dict[str, str] = {}

    type: PaymentMethodType
