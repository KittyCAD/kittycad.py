from pydantic import BaseModel, ConfigDict


class Sceneclearall(BaseModel):
    """The response from the `SceneClearAll` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
