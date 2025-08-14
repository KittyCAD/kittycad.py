from pydantic import BaseModel, ConfigDict


class Selectreplace(BaseModel):
    """The response from the `SelectReplace` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
