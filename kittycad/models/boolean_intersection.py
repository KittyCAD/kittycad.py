from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class BooleanIntersection(BaseModel):
    """The response from the 'BooleanIntersection'."""

    extra_solid_ids: Optional[List[str]] = None

    model_config = ConfigDict(protected_namespaces=())
