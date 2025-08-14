from pydantic import BaseModel, ConfigDict


class Paymentintent(BaseModel):
    """A payment intent response."""

    client_secret: str

    model_config = ConfigDict(protected_namespaces=())
