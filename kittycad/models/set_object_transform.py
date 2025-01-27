from pydantic import BaseModel, ConfigDict


class SetObjectTransform(BaseModel):
    """The response from the `SetObjectTransform` command."""

    model_config = ConfigDict(protected_namespaces=())
