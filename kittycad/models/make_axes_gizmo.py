from pydantic import BaseModel, ConfigDict


class Makeaxesgizmo(BaseModel):
    """The response from the `MakeAxesGizmo` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
