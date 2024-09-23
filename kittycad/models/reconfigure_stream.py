from pydantic import BaseModel, ConfigDict


class ReconfigureStream(BaseModel):
    """The response from the `ReconfigureStream` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
