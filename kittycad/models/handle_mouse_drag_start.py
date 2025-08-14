from pydantic import BaseModel, ConfigDict


class HandleMouseDragStart(BaseModel):
    """The response from the `HandleMouseDragStart` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
