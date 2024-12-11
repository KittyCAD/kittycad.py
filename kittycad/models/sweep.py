from pydantic import BaseModel, ConfigDict


class Sweep(BaseModel):
    """The response from the `Sweep` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
