
from pydantic import BaseModel



class EntityGetDistance(BaseModel):
    """The response from the `EntitiesGetDistance` command."""

    max_distance: float

    min_distance: float
