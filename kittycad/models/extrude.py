from pydantic import BaseModel, ConfigDict


class Extrude(BaseModel):
    """The response from the `Extrude` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
