from pydantic import BaseModel, ConfigDict


class Newannotation(BaseModel):
    """The response from the `NewAnnotation` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
