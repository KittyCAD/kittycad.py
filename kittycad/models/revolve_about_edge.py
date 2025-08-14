from pydantic import BaseModel, ConfigDict


class RevolveAboutEdge(BaseModel):
    """The response from the `RevolveAboutEdge` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
