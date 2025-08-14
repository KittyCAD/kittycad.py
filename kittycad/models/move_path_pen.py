from pydantic import BaseModel, ConfigDict


class Movepathpen(BaseModel):
    """The response from the `MovePathPen` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
