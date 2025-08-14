from pydantic import BaseModel, ConfigDict


class HandleMouseDragMove(BaseModel):
    """The response from the `HandleMouseDragMove` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
