
from pydantic import BaseModel, ConfigDict



class Color(BaseModel):
    """An RGBA color"""

    a: float

    b: float

    g: float

    r: float

    model_config = ConfigDict(protected_namespaces=())
