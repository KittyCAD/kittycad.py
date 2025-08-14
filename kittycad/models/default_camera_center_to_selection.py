from pydantic import BaseModel, ConfigDict


class Defaultcameracentertoselection(BaseModel):
    """The response from the `DefaultCameraCenterToSelection` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
