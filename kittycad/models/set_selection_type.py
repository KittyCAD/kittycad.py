from pydantic import BaseModel, ConfigDict


class Setselectiontype(BaseModel):
    """The response from the `SetSelectionType` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
