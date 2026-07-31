from typing import List

from .base import KittyCadBaseModel


class CreatePlanarSurface(KittyCadBaseModel):
    """The response from the 'CreatePlanarSurface'."""

    surfaces: List[str]
