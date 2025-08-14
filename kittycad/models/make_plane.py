from pydantic import BaseModel, ConfigDict


class MakePlane(BaseModel):
    """The response from the `MakePlane` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
