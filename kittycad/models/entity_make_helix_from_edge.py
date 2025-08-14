from pydantic import BaseModel, ConfigDict


class Entitymakehelixfromedge(BaseModel):
    """The response from the `EntityMakeHelixFromEdge` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
