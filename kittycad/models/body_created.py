from typing import List

from ..models.surface_created import SurfaceCreated
from .base import KittyCadBaseModel


class BodyCreated(KittyCadBaseModel):
    """Details of a body that was created."""

    id: str

    surfaces: List[SurfaceCreated]
