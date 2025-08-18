from typing import List

from .base import KittyCadBaseModel


class PathGetCurveUuidsForVertices(KittyCadBaseModel):
    """The response from the `PathGetCurveUuidsForVertices` command."""

    curve_ids: List[str]
