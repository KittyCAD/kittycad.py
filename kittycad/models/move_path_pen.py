from pydantic import BaseModel, ConfigDict


class MovePathPen(BaseModel):
    """The response from the `MovePathPen` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
