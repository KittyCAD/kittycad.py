
from pydantic import BaseModel, ConfigDict



class EntityGetDistance(BaseModel):
    """The response from the `EntitiesGetDistance` command."""

    max_distance: float

    min_distance: float

    model_config = ConfigDict(protected_namespaces=())
