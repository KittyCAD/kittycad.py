from pydantic import BaseModel, ConfigDict


class Reconfigurestream(BaseModel):
    """The response from the `ReconfigureStream` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
