import datetime
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, Base64Bytes, BaseModel, ConfigDict
from pydantic_extra_types.phone_numbers import PhoneNumber

from .base64data import Base64Data


class PaymentMethodCardChecks(BaseModel):
    """Card checks."""

    address_line1_check: Optional[str] = None

    address_postal_code_check: Optional[str] = None

    cvc_check: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
