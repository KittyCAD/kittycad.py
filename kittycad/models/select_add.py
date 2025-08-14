from pydantic import BaseModel, ConfigDict


class Selectadd(BaseModel):
    """The response from the `SelectAdd` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
