
from pydantic import BaseModel, ConfigDict

from .base64data import Base64Data


class TakeSnapshot(BaseModel):
    """The response from the `TakeSnapshot` command."""

    contents: Base64Data

    model_config = ConfigDict(protected_namespaces=())
