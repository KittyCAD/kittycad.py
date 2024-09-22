from pydantic import BaseModel, ConfigDict


class HighlightSetEntities(BaseModel):
    """The response from the `HighlightSetEntities` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
