from pydantic import BaseModel, ConfigDict


class UpdateAnnotation(BaseModel):
    """The response from the `UpdateAnnotation` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
