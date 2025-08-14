from typing import Optional

from pydantic import BaseModel, ConfigDict


class UpdatePaymentBalance(BaseModel):
    """The data for updating a balance."""

    monthly_api_credits_remaining_monetary_value: Optional[float] = None

    stable_api_credits_remaining_monetary_value: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
