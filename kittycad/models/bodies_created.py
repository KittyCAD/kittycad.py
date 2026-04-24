from typing import List

from ..models.body_created import BodyCreated
from .base import KittyCadBaseModel


class BodiesCreated(KittyCadBaseModel):
    """List of bodies that were created by an operation."""

    bodies: List[BodyCreated]
