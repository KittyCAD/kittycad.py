
from pydantic import BaseModel, ConfigDict



class Point3d(BaseModel):
    """A point in 3D space"""

    x: float

    y: float

    z: float

    model_config = ConfigDict(protected_namespaces=())
