from pydantic import BaseModel, ConfigDict


class Setselectionfilter(BaseModel):
    """The response from the `SetSelectionFilter` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
