from typing import List

from pydantic import BaseModel, ConfigDict


class Entitygetsketchpaths(BaseModel):
    """The response from the `EntityGetSketchPaths` command."""

    entity_ids: List[str]

    model_config = ConfigDict(protected_namespaces=())
