from pydantic import BaseModel, ConfigDict


class Solid3dFilletEdge(BaseModel):
    """The response from the `Solid3dFilletEdge` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
