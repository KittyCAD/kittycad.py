from typing import List

from pydantic import BaseModel, ConfigDict


class BooleanIntersection(BaseModel):
    """The response from the 'BooleanIntersection'."""

    extra_solid_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
