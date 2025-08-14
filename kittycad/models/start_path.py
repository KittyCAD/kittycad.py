from pydantic import BaseModel, ConfigDict


class Startpath(BaseModel):
    """The response from the `StartPath` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
