
from pydantic import BaseModel



class EntityGetNumChildren(BaseModel):
    """The response from the `EntityGetNumChildren` command."""

    num: int
