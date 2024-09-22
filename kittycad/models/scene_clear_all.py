from pydantic import BaseModel, ConfigDict


class SceneClearAll(BaseModel):
    """The response from the `SceneClearAll` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
