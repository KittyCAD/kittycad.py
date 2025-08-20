from ..models.coupon import Coupon
from .base import KittyCadBaseModel


class Discount(KittyCadBaseModel):
    """The resource representing a Discount."""

    coupon: Coupon
