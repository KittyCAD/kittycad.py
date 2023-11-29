
from pydantic import BaseModel

from .base64data import Base64Data


class TakeSnapshot(BaseModel):
    """The response from the `TakeSnapshot` command."""

    contents: Base64Data
