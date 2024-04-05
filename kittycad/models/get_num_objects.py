
from pydantic import BaseModel, ConfigDict



class GetNumObjects(BaseModel):
    """The response from the `GetNumObjects` command."""

    num_objects: int

    model_config = ConfigDict(protected_namespaces=())
