from .base import KittyCadBaseModel


class Point3d(KittyCadBaseModel):
    """A point in 3D space"""

    x: float

    y: float

    z: float
