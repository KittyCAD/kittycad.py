from .base import KittyCadBaseModel


class ImportFile(KittyCadBaseModel):
    """File to import into the current model. If you are sending binary data for a file, be sure to send the WebSocketRequest as binary/bson, not text/json."""

    data: bytes

    path: str
