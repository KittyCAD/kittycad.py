from pydantic import BaseModel, ConfigDict


class Extendpath(BaseModel):
    """The response from the `ExtendPath` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
