
from pydantic import BaseModel



class Point3d(BaseModel):
    """A point in 3D space"""

    x: float

    y: float

    z: float
