import datetime

from pydantic import BaseModel, ConfigDict

from ..models.uuid import Uuid


class CustomerBalance(BaseModel):
    """A balance for a customer.

    This holds information about the financial balance for the customer."""

    created_at: datetime.datetime

    id: Uuid

    map_id: Uuid

    monthly_credits_remaining: float

    pre_pay_cash_remaining: float

    pre_pay_credits_remaining: float

    total_due: float

    updated_at: datetime.datetime

    model_config = ConfigDict(protected_namespaces=())
