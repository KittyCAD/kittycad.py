from pydantic import BaseModel, ConfigDict


class Setcurrenttoolproperties(BaseModel):
    """The response from the `SetCurrentToolProperties` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
