from .base import KittyCadBaseModel


class Solid3dGetOppositeEdge(KittyCadBaseModel):
    """The response from the `Solid3dGetOppositeEdge` command."""

    edge: str
