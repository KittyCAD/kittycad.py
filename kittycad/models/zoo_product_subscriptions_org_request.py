from typing import Optional

from .base import KittyCadBaseModel


class ZooProductSubscriptionsOrgRequest(KittyCadBaseModel):
    """A struct of Zoo product subscriptions an organization can request."""

    modeling_app: str

    pay_annually: Optional[bool] = None
