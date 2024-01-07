from typing import List

from pydantic import BaseModel, ConfigDict



class Solid3dGetAllOppositeEdges(BaseModel):
    """The response from the `Solid3dGetAllOppositeEdges` command."""

    edges: List[str]

    model_config = ConfigDict(protected_namespaces=())
