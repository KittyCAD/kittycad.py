from .base import KittyCadBaseModel


class Subscribe(KittyCadBaseModel):
    """The data for subscribing a user to the newsletter."""

    email: str
