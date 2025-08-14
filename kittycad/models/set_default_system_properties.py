from pydantic import BaseModel, ConfigDict


class Setdefaultsystemproperties(BaseModel):
    """The response from the `SetDefaultSystemProperties` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
