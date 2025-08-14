from pydantic import BaseModel, ConfigDict


class Getnumobjects(BaseModel):
    """The response from the `GetNumObjects` command."""

    num_objects: int

    model_config = ConfigDict(protected_namespaces=())
