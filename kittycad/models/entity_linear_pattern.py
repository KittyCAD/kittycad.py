from typing import List

from pydantic import BaseModel, ConfigDict



class EntityLinearPattern(BaseModel):
    """The response from the `EntityLinearPattern` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
