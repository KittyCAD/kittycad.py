from pydantic import BaseModel, ConfigDict


class SetDefaultSystemProperties(BaseModel):
    """The response from the `SetDefaultSystemProperties` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
