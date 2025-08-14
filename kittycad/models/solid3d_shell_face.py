from pydantic import BaseModel, ConfigDict


class Solid3dShellFace(BaseModel):
    """The response from the `Solid3dShellFace` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
