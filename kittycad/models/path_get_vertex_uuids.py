from typing import List

from pydantic import BaseModel, ConfigDict



class PathGetVertexUuids(BaseModel):
    """The response from the `PathGetVertexUuids` command."""

    vertex_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
