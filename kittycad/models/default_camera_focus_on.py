from pydantic import BaseModel, ConfigDict


class Defaultcamerafocuson(BaseModel):
    """The response from the `DefaultCameraFocusOn` command."""

    model_config = ConfigDict(protected_namespaces=())
