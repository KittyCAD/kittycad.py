
from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d


class LinearTransform(BaseModel):
    """Ways to transform each solid being replicated in a repeating pattern."""

    replicate: bool = True

    scale: Point3d = {"x": 1.0, "y": 1.0, "z": 1.0}

    translate: Point3d = {"x": 0.0, "y": 0.0, "z": 0.0}

    model_config = ConfigDict(protected_namespaces=())
