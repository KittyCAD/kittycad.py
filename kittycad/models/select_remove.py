from pydantic import BaseModel, ConfigDict


class Selectremove(BaseModel):
    """The response from the `SelectRemove` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
