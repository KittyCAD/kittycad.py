from pydantic import BaseModel, ConfigDict


class Handlemousedragstart(BaseModel):
    """The response from the `HandleMouseDragStart` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
