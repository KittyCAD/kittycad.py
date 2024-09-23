from pydantic import BaseModel, ConfigDict


class SelectAdd(BaseModel):
    """The response from the `SelectAdd` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
