from pydantic import BaseModel, ConfigDict


class Revolve(BaseModel):
    """The response from the `Revolve` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
