from pydantic import BaseModel, ConfigDict


class Setgridautoscale(BaseModel):
    """The response from the 'SetGridScale'."""

    model_config = ConfigDict(protected_namespaces=())
