from .base import KittyCadBaseModel


class Point4d(KittyCadBaseModel):
    """A point in homogeneous (4D) space"""

    w: float

    x: float

    y: float

    z: float
