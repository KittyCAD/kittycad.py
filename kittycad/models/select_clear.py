from pydantic import BaseModel, ConfigDict


class Selectclear(BaseModel):
    """The response from the `SelectClear` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
