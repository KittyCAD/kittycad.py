
from pydantic import BaseModel, ConfigDict



class ClosePath(BaseModel):
    """The response from the `ClosePath` command."""

    face_id: str

    model_config = ConfigDict(protected_namespaces=())
