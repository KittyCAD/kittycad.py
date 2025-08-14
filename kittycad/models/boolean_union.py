from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Booleanunion(BaseModel):
    """The response from the 'BooleanUnion'."""

    extra_solid_ids: Optional[List[str]] = None

    model_config = ConfigDict(protected_namespaces=())
