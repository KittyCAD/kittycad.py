from pydantic import BaseModel, ConfigDict


class SelectClear(BaseModel):
    """The response from the `SelectClear` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
