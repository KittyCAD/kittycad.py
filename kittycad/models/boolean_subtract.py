from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class BooleanSubtract(BaseModel):
    """The response from the 'BooleanSubtract'."""

    extra_solid_ids: Optional[List[str]] = None

    model_config = ConfigDict(protected_namespaces=())
