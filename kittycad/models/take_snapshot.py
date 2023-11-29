
from pydantic import Base64Bytes, BaseModel


class TakeSnapshot(BaseModel):
    """The response from the `TakeSnapshot` command."""

    contents: Base64Bytes
