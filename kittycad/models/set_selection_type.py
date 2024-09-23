from pydantic import BaseModel, ConfigDict


class SetSelectionType(BaseModel):
    """The response from the `SetSelectionType` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
