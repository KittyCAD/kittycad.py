from .base import KittyCadBaseModel


class Color(KittyCadBaseModel):
    """An RGBA color"""

    a: float

    b: float

    g: float

    r: float
