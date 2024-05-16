
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class FaceGetCenter(BaseModel):
    """The 3D center of mass on the surface"""

    pos: Point3d

    model_config = ConfigDict(protected_namespaces=())
