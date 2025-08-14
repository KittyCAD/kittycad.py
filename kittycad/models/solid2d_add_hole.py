from pydantic import BaseModel, ConfigDict


class Solid2dAddHole(BaseModel):
    """The response from the `Solid2dAddHole` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
