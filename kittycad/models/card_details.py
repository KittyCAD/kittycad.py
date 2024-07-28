import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from ..models.payment_method_card_checks import PaymentMethodCardChecks
from .base64data import Base64Data


class CardDetails(BaseModel):
    """The card details of a payment method."""

    brand: Optional[str] = None

    checks: Optional[PaymentMethodCardChecks] = None

    country: Optional[str] = None

    exp_month: Optional[int] = None

    exp_year: Optional[int] = None

    fingerprint: Optional[str] = None

    funding: Optional[str] = None

    last4: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
