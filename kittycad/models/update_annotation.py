from pydantic import BaseModel, ConfigDict


class Updateannotation(BaseModel):
    """The response from the `UpdateAnnotation` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
