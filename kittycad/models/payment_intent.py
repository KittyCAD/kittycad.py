
from pydantic import BaseModel



class PaymentIntent(BaseModel):
    """A payment intent response."""

    client_secret: str
