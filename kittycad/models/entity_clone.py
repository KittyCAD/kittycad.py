from pydantic import BaseModel, ConfigDict


class EntityClone(BaseModel):
    """The response from the `EntityClone` command."""

    model_config = ConfigDict(protected_namespaces=())
