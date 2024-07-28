
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class CurveGetEndPoints(BaseModel):
    """Endpoints of a curve"""

    end: Point3d

    start: Point3d

    model_config = ConfigDict(protected_namespaces=())
