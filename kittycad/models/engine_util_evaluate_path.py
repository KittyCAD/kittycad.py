from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class EngineUtilEvaluatePath(BaseModel):
    """The response of the `EngineUtilEvaluatePath` endpoint"""

    pos: Point3d

    model_config = ConfigDict(protected_namespaces=())
