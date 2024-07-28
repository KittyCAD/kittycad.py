import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class UpdatePaymentBalance(BaseModel):
    """The data for updating a balance."""

    monthly_credits_remaining: Optional[float] = None

    pre_pay_cash_remaining: Optional[float] = None

    pre_pay_credits_remaining: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
