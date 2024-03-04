from typing import List

from pydantic import BaseModel, ConfigDict



class EntityCircularPattern(BaseModel):
    """The response from the `EntityCircularPattern` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
