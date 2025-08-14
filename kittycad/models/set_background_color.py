from pydantic import BaseModel, ConfigDict


class Setbackgroundcolor(BaseModel):
    """The response from the `SetBackgroundColor` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
