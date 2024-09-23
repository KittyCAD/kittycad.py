from pydantic import BaseModel, ConfigDict


class EdgeLinesVisible(BaseModel):
    """The response from the `EdgeLinesVisible` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
