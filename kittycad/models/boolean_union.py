from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class BooleanUnion(BaseModel):
    """The response from the 'BooleanUnion'."""

    extra_solid_ids: Optional[List[str]] = None

    model_config = ConfigDict(protected_namespaces=())
