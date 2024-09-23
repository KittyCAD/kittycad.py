from pydantic import BaseModel, ConfigDict


class EntityFade(BaseModel):
    """The response from the `EntityFade` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
