from typing import Dict, Optional

from .base import KittyCadBaseModel


class Coupon(KittyCadBaseModel):
    """The resource representing a Coupon."""

    amount_off: Optional[float] = None

    deleted: Optional[bool] = False

    id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = {}

    name: Optional[str] = None

    percent_off: Optional[float] = None
