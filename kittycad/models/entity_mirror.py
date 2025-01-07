from typing import List

from pydantic import BaseModel, ConfigDict


class EntityMirror(BaseModel):
    """The response from the `EntityMirror` endpoint."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
