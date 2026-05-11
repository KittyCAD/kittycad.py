from typing import Optional

from ..models.edge_specifier import EdgeSpecifier
from .base import KittyCadBaseModel


class FractionOfEdge(KittyCadBaseModel):
    """An edge id and an upper and lower percentage bound of the edge."""

    edge_id: Optional[str] = None

    edge_specifier: Optional[EdgeSpecifier] = None

    lower_bound: Optional[float] = 0.0

    upper_bound: Optional[float] = 1.0
