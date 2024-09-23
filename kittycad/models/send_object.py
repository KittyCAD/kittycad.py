from pydantic import BaseModel, ConfigDict


class SendObject(BaseModel):
    """The response from the `SendObject` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
