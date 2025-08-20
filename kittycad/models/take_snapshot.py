from .base import KittyCadBaseModel
from .base64data import Base64Data


class TakeSnapshot(KittyCadBaseModel):
    """The response from the `TakeSnapshot` command."""

    contents: Base64Data
