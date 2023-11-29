
from pydantic import BaseModel



class Color(BaseModel):
    """An RGBA color"""

    a: float

    b: float

    g: float

    r: float
