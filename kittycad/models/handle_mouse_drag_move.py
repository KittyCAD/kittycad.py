from pydantic import BaseModel, ConfigDict


class Handlemousedragmove(BaseModel):
    """The response from the `HandleMouseDragMove` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
