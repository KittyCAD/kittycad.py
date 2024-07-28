from typing import Optional

from pydantic import BaseModel, ConfigDict



class HighlightSetEntity(BaseModel):
    """The response from the `HighlightSetEntity` command."""

    entity_id: Optional[str] = None

    sequence: Optional[int] = None

    model_config = ConfigDict(protected_namespaces=())
