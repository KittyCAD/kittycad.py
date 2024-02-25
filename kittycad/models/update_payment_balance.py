from typing import Optional

from pydantic import BaseModel, ConfigDict



class UpdatePaymentBalance(BaseModel):
    """The data for updating a balance."""

    monthly_credits_remaining: Optional[float] = None

    pre_pay_cash_remaining: Optional[float] = None

    pre_pay_credits_remaining: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
