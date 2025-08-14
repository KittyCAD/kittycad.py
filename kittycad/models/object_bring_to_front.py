from pydantic import BaseModel, ConfigDict


class Objectbringtofront(BaseModel):
    """The response from the `ObjectBringToFront` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
