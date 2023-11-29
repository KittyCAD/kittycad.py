
from pydantic import BaseModel



class Point2d(BaseModel):
    """A point in 2D space"""

    x: float

    y: float
