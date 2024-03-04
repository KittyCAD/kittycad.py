from typing import List

from pydantic import BaseModel, ConfigDict



class MouseClick(BaseModel):
    """The response from the `MouseClick` command."""

    entities_modified: List[str]

    entities_selected: List[str]

    model_config = ConfigDict(protected_namespaces=())
