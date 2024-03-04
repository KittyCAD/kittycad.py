
from pydantic import BaseModel, ConfigDict



class Pong(BaseModel):
    """The response from the `/ping` endpoint."""

    message: str

    model_config = ConfigDict(protected_namespaces=())
