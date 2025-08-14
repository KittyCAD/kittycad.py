from pydantic import BaseModel, ConfigDict


class Setobjecttransform(BaseModel):
    """The response from the `SetObjectTransform` command."""

    model_config = ConfigDict(protected_namespaces=())
