from typing import List

from pydantic import BaseModel, ConfigDict


class Makeoffsetpath(BaseModel):
    """The response from the `MakeOffsetPath` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
