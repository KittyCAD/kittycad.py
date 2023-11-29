
from pydantic import BaseModel



class Pong(BaseModel):
    """The response from the `/ping` endpoint."""

    message: str
