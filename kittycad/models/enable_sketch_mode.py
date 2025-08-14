from pydantic import BaseModel, ConfigDict


class Enablesketchmode(BaseModel):
    """The response from the `EnableSketchMode` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
