from pydantic import BaseModel, ConfigDict


class NewAnnotation(BaseModel):
    """The response from the `NewAnnotation` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
