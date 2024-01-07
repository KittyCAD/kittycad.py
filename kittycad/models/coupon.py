from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict



class Coupon(BaseModel):
    """The resource representing a Coupon."""

    amount_off: Optional[float] = None

    deleted: Optional[bool] = None

    id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    percent_off: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
