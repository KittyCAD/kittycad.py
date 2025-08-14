from pydantic import BaseModel, ConfigDict


class Highlightsetentities(BaseModel):
    """The response from the `HighlightSetEntities` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
