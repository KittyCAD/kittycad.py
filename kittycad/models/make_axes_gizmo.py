from pydantic import BaseModel, ConfigDict


class MakeAxesGizmo(BaseModel):
    """The response from the `MakeAxesGizmo` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
