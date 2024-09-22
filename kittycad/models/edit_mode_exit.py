from pydantic import BaseModel, ConfigDict


class EditModeExit(BaseModel):
    """The response from the `EditModeExit` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
