from pydantic import BaseModel, ConfigDict


class Settool(BaseModel):
    """The response from the `SetTool` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
