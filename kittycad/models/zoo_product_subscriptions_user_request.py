from typing import Optional

from .base import KittyCadBaseModel


class ZooProductSubscriptionsUserRequest(KittyCadBaseModel):
    """A struct of Zoo product subscriptions a user can request."""

    modeling_app: str

    pay_annually: Optional[bool] = None
