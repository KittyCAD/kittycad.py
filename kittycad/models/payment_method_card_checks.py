from typing import Optional

from pydantic import BaseModel, ConfigDict



class PaymentMethodCardChecks(BaseModel):
    """Card checks."""

    address_line1_check: Optional[str] = None

    address_postal_code_check: Optional[str] = None

    cvc_check: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
