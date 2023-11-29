import datetime

from pydantic import BaseModel

from ..models.uuid import Uuid


class CustomerBalance(BaseModel):
    """A balance for a user.

    This holds information about the financial balance for the user."""

    created_at: datetime.datetime

    id: Uuid

    monthly_credits_remaining: float

    pre_pay_cash_remaining: float

    pre_pay_credits_remaining: float

    total_due: float

    updated_at: datetime.datetime

    user_id: Uuid
