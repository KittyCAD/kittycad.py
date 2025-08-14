from pydantic import BaseModel, ConfigDict


class Subscriptiontierfeature(BaseModel):
    """A subscription tier feature."""

    info: str

    model_config = ConfigDict(protected_namespaces=())
