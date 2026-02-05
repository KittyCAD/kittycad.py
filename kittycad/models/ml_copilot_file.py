from .base import KittyCadBaseModel


class MlCopilotFile(KittyCadBaseModel):
    """A file that can be transferred between the client and server."""

    data: bytes

    mimetype: str

    name: str
