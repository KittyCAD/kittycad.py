from .base import KittyCadBaseModel


class Pong(KittyCadBaseModel):
    """The response from the `/ping` endpoint."""

    message: str
