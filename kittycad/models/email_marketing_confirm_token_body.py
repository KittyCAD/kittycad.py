from .base import KittyCadBaseModel


class EmailMarketingConfirmTokenBody(KittyCadBaseModel):
    """Request payload for confirming a double-opt-in token."""

    token: str
