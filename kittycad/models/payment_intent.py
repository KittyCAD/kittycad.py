from .base import KittyCadBaseModel


class PaymentIntent(KittyCadBaseModel):
    """A payment intent response."""

    client_secret: str
