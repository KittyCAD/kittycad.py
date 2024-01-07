
from pydantic import BaseModel, ConfigDict



class EntityGetNumChildren(BaseModel):
    """The response from the `EntityGetNumChildren` command."""

    num: int

    model_config = ConfigDict(protected_namespaces=())
