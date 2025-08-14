from pydantic import BaseModel, ConfigDict


class Storecouponparams(BaseModel):
    """The parameters for a new store coupon."""

    percent_off: int

    model_config = ConfigDict(protected_namespaces=())
