from .base import KittyCadBaseModel


class Solid3dGetEdgeUuid(KittyCadBaseModel):
    """The response from the `Solid3dGetEdgeUuid` endpoint."""

    edge_id: str
