
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class FaceGetGradient(BaseModel):
    """The gradient (dFdu, dFdv) + normal vector on a brep face"""

    df_du: Point3d

    df_dv: Point3d

    normal: Point3d

    model_config = ConfigDict(protected_namespaces=())
