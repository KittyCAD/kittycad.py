from pydantic import BaseModel, ConfigDict


class EnableDryRun(BaseModel):
    """The response from the `EnableDryRun` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
