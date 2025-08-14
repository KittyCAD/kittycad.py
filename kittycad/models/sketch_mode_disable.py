from pydantic import BaseModel, ConfigDict


class SketchModeDisable(BaseModel):
    """The response from the `SketchModeDisable` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
