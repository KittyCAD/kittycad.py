from typing import Optional

from pydantic import BaseModel, ConfigDict


class Selectwithpoint(BaseModel):
    """The response from the `SelectWithPoint` command."""

    entity_id: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
