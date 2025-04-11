from typing import List

from pydantic import BaseModel, ConfigDict


class BooleanSubtract(BaseModel):
    """The response from the 'BooleanSubtract'."""

    extra_solid_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
