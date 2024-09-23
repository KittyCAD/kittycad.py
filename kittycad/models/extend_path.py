from pydantic import BaseModel, ConfigDict


class ExtendPath(BaseModel):
    """The response from the `ExtendPath` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
