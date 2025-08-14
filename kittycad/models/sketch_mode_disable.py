from pydantic import BaseModel, ConfigDict


class Sketchmodedisable(BaseModel):
    """The response from the `SketchModeDisable` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
