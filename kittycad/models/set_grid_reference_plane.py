from pydantic import BaseModel, ConfigDict


class SetGridReferencePlane(BaseModel):
    """The response from the 'SetGridReferencePlane'."""

    model_config = ConfigDict(protected_namespaces=())
