from typing import List

from ..models.surface_created import SurfaceCreated
from .base import KittyCadBaseModel


class BodyUpdated(KittyCadBaseModel):
    """Details of a body that was updated."""

    id: str

    surfaces: List[SurfaceCreated]
