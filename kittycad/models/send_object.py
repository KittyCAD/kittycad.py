from pydantic import BaseModel, ConfigDict


class Sendobject(BaseModel):
    """The response from the `SendObject` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
