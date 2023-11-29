
from pydantic import BaseModel

from ..models.coupon import Coupon


class Discount(BaseModel):
    """The resource representing a Discount."""

    coupon: Coupon
