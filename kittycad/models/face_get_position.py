
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class FaceGetPosition(BaseModel):
    """The 3D position on the surface that was evaluated"""

    pos: Point3d

    model_config = ConfigDict(protected_namespaces=())
