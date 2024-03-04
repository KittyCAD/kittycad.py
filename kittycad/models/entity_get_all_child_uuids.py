from typing import List

from pydantic import BaseModel, ConfigDict



class EntityGetAllChildUuids(BaseModel):
    """The response from the `EntityGetAllChildUuids` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
