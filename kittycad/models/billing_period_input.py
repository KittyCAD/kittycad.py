import datetime
from typing import Optional

from ..models.billing_period_index import BillingPeriodIndex
from ..models.billing_period_status import BillingPeriodStatus
from .base import KittyCadBaseModel


class BillingPeriodInput(KittyCadBaseModel):
    """Serialized billing period payload for a contract definition."""

    commitment_amount: float

    period_end_at: datetime.datetime

    period_index: BillingPeriodIndex

    period_start_at: datetime.datetime

    rollover_in_amount: Optional[float] = None

    rollover_out_amount: Optional[float] = None

    status: Optional[BillingPeriodStatus] = None
