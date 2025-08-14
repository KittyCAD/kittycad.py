from pydantic import BaseModel, ConfigDict


class Revolveaboutedge(BaseModel):
    """The response from the `RevolveAboutEdge` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
