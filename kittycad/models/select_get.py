from typing import List

from pydantic import BaseModel, ConfigDict


class Selectget(BaseModel):
    """The response from the `SelectGet` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
