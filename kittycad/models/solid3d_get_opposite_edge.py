
from pydantic import BaseModel



class Solid3dGetOppositeEdge(BaseModel):
    """The response from the `Solid3dGetOppositeEdge` command."""

    edge: str
