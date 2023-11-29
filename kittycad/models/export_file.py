
from pydantic import BaseModel

from .base64data import Base64Data


class ExportFile(BaseModel):
    """A file to be exported to the client."""

    contents: Base64Data

    name: str
