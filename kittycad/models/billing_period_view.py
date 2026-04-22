import datetime

from ..models.billing_period_index import BillingPeriodIndex
from ..models.billing_period_status import BillingPeriodStatus
from ..models.uuid import Uuid
from .base import KittyCadBaseModel


class BillingPeriodView(KittyCadBaseModel):
    """Serialized billing period returned from a stored contract."""

    commitment_amount: float

    id: Uuid

    period_end_at: datetime.datetime

    period_index: BillingPeriodIndex

    period_start_at: datetime.datetime

    rollover_in_amount: float

    rollover_out_amount: float

    status: BillingPeriodStatus
