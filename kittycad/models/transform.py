from ..models.point3d import Point3d
from ..models.rotation import Rotation
from .base import KittyCadBaseModel


class Transform(KittyCadBaseModel):
    """Ways to transform each solid being replicated in a repeating pattern."""

    replicate: bool = True

    rotation: Rotation = {
        "angle": {"unit": "degrees", "value": 0.0},
        "axis": {"x": 0.0, "y": 0.0, "z": 1.0},
        "origin": {"type": "local"},
    }  # type: ignore[assignment]

    scale: Point3d = {"x": 1.0, "y": 1.0, "z": 1.0}  # type: ignore[assignment]

    translate: Point3d = {"x": 0.0, "y": 0.0, "z": 0.0}  # type: ignore[assignment]
