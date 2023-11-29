from typing import Optional

from pydantic import BaseModel



class Coupon(BaseModel):
    """The resource representing a Coupon."""

    amount_off: Optional[float] = None

    deleted: Optional[bool] = None

    id: Optional[str] = None

    percent_off: Optional[float] = None
