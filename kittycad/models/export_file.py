
from pydantic import Base64Bytes, BaseModel


class ExportFile(BaseModel):
    """A file to be exported to the client."""

    contents: Base64Bytes

    name: str
