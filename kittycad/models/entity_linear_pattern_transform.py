from typing import List

from pydantic import BaseModel, ConfigDict



class EntityLinearPatternTransform(BaseModel):
    """The response from the `EntityLinearPatternTransform` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
