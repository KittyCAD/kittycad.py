from pydantic import BaseModel, ConfigDict


class SelectReplace(BaseModel):
    """The response from the `SelectReplace` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
