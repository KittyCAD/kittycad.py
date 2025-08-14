from pydantic import BaseModel, ConfigDict


class Objectvisible(BaseModel):
    """The response from the `ObjectVisible` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
