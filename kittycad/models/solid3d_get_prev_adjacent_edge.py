from typing import Optional

from pydantic import BaseModel, ConfigDict


class Solid3dgetprevadjacentedge(BaseModel):
    """The response from the `Solid3dGetPrevAdjacentEdge` command."""

    edge: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
