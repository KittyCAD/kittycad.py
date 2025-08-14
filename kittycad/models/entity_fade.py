from pydantic import BaseModel, ConfigDict


class Entityfade(BaseModel):
    """The response from the `EntityFade` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
