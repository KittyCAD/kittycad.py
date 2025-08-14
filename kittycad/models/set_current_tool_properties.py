from pydantic import BaseModel, ConfigDict


class SetCurrentToolProperties(BaseModel):
    """The response from the `SetCurrentToolProperties` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
