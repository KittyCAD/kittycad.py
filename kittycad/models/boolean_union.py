from typing import List

from pydantic import BaseModel, ConfigDict


class BooleanUnion(BaseModel):
    """The response from the 'BooleanUnion'."""

    extra_solid_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
