from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class Engineutilevaluatepath(BaseModel):
    """The response of the `EngineUtilEvaluatePath` endpoint"""

    pos: Point3d

    model_config = ConfigDict(protected_namespaces=())
