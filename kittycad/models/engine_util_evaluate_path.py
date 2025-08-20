from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class EngineUtilEvaluatePath(KittyCadBaseModel):
    """The response of the `EngineUtilEvaluatePath` endpoint"""

    pos: Point3d
