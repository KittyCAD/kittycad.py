from pydantic import BaseModel, ConfigDict


class Mousemove(BaseModel):
    """The response from the `MouseMove` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
