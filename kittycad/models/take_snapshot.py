from pydantic import BaseModel, ConfigDict

from .base64data import Base64Data


class Takesnapshot(BaseModel):
    """The response from the `TakeSnapshot` command."""

    contents: Base64Data

    model_config = ConfigDict(protected_namespaces=())
