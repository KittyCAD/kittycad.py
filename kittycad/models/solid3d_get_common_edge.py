from typing import Optional

from pydantic import BaseModel, ConfigDict


class Solid3dGetCommonEdge(BaseModel):
    """The response from the `Solid3DGetCommonEdge` command."""

    edge: Optional[str] = None

    model_config = ConfigDict(protected_namespaces=())
