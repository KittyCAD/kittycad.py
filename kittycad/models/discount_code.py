import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict



class DiscountCode(BaseModel):
    """A discount code for a store."""

    code: str

    expires_at: Optional[datetime.datetime] = None

    percent_off: int

    model_config = ConfigDict(protected_namespaces=())
