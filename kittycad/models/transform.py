from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d
from ..models.rotation import Rotation


class Transform(BaseModel):
    """Ways to transform each solid being replicated in a repeating pattern."""

    replicate: bool = True

    rotation: Rotation = {
        "angle": {"unit": "degrees", "value": 0.0},
        "axis": {"x": 0.0, "y": 0.0, "z": 1.0},
        "origin": {"type": "local"},
    }  # type: ignore

    scale: Point3d = {"x": 1.0, "y": 1.0, "z": 1.0}  # type: ignore

    translate: Point3d = {"x": 0.0, "y": 0.0, "z": 0.0}  # type: ignore

    model_config = ConfigDict(protected_namespaces=())
