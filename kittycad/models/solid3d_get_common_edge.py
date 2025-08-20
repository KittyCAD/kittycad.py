from typing import Optional

from .base import KittyCadBaseModel


class Solid3dGetCommonEdge(KittyCadBaseModel):
    """The response from the `Solid3DGetCommonEdge` command."""

    edge: Optional[str] = None
