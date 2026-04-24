from typing import Optional

from ..models.bodies_created import BodiesCreated
from ..models.bodies_updated import BodiesUpdated
from .base import KittyCadBaseModel


class RevolveAboutEdge(KittyCadBaseModel):
    """The response from the `RevolveAboutEdge` endpoint."""

    bodies_created: Optional[BodiesCreated] = None

    bodies_updated: Optional[BodiesUpdated] = None
