from typing import List

from ..models.body_updated import BodyUpdated
from .base import KittyCadBaseModel


class BodiesUpdated(KittyCadBaseModel):
    """List of bodies that were updated by an operation."""

    bodies: List[BodyUpdated]
