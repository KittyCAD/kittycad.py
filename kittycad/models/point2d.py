
from pydantic import BaseModel, ConfigDict



class Point2d(BaseModel):
    """A point in 2D space"""

    x: float

    y: float

    model_config = ConfigDict(protected_namespaces=())
