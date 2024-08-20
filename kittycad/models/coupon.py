from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict



class Coupon(BaseModel):
    """The resource representing a Coupon."""

    amount_off: Optional[float] = None

    deleted: bool = False

    id: Optional[str] = None

    metadata: Dict[str, str] = {}

    name: Optional[str] = None

    percent_off: Optional[float] = None

    model_config = ConfigDict(protected_namespaces=())
