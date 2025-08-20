from .base import KittyCadBaseModel
from .base64data import Base64Data


class ExportFile(KittyCadBaseModel):
    """A file to be exported to the client."""

    contents: Base64Data

    name: str
