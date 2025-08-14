from pydantic import BaseModel, ConfigDict


class Handlemousedragend(BaseModel):
    """The response from the `HandleMouseDragEnd` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
