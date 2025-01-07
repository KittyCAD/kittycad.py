from typing import List

from pydantic import BaseModel, ConfigDict


class AddHoleFromOffset(BaseModel):
    """The response from the `AddHoleFromOffset` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
