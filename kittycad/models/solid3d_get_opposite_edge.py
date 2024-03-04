
from pydantic import BaseModel, ConfigDict



class Solid3dGetOppositeEdge(BaseModel):
    """The response from the `Solid3dGetOppositeEdge` command."""

    edge: str

    model_config = ConfigDict(protected_namespaces=())
