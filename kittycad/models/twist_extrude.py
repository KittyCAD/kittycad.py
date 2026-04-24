from typing import Optional

from ..models.bodies_created import BodiesCreated
from ..models.bodies_updated import BodiesUpdated
from .base import KittyCadBaseModel


class TwistExtrude(KittyCadBaseModel):
    """The response from the `TwistExtrude` endpoint."""

    bodies_created: Optional[BodiesCreated] = None

    bodies_updated: Optional[BodiesUpdated] = None
