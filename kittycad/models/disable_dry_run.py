from pydantic import BaseModel, ConfigDict


class DisableDryRun(BaseModel):
    """The response from the `DisableDryRun` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
