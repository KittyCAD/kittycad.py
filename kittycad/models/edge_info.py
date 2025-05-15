from typing import List

from pydantic import BaseModel, ConfigDict


class EdgeInfo(BaseModel):
    """A list of faces for a specific edge."""

    edge_id: str

    faces: List[str]

    model_config = ConfigDict(protected_namespaces=())
