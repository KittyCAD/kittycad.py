
from pydantic import BaseModel, ConfigDict

from ..models.coupon import Coupon


class Discount(BaseModel):
    """The resource representing a Discount."""

    coupon: Coupon

    model_config = ConfigDict(protected_namespaces=())
