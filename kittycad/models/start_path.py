from pydantic import BaseModel, ConfigDict


class StartPath(BaseModel):
    """The response from the `StartPath` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
