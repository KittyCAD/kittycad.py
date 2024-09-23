from pydantic import BaseModel, ConfigDict


class EditModeEnter(BaseModel):
    """The response from the `EditModeEnter` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
