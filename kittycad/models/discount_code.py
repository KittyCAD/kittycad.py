import datetime
from typing import Optional

from .base import KittyCadBaseModel


class DiscountCode(KittyCadBaseModel):
    """A discount code for a store."""

    code: str

    expires_at: Optional[datetime.datetime] = None

    percent_off: int
