from pydantic import BaseModel, ConfigDict


class MouseMove(BaseModel):
    """The response from the `MouseMove` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
