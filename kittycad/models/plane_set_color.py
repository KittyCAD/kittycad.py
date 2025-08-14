from pydantic import BaseModel, ConfigDict


class Planesetcolor(BaseModel):
    """The response from the `PlaneSetColor` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
