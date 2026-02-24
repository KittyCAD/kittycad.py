from .base import KittyCadBaseModel


class FractionOfEdge(KittyCadBaseModel):
    """An edge id and an upper and lower percentage bound of the edge."""

    edge_id: str

    lower_bound: float = 0.0

    upper_bound: float = 1.0
