from .base import KittyCadBaseModel


class StoreCouponParams(KittyCadBaseModel):
    """The parameters for a new store coupon."""

    percent_off: int
