from .base import KittyCadBaseModel


class ClosePath(KittyCadBaseModel):
    """The response from the `ClosePath` command."""

    face_id: str
