
from pydantic import BaseModel, ConfigDict



class Point4d(BaseModel):
    """A point in homogeneous (4D) space"""

    w: float

    x: float

    y: float

    z: float

    model_config = ConfigDict(protected_namespaces=())
