from pydantic import BaseModel, ConfigDict


class SetGridAutoScale(BaseModel):
    """The response from the 'SetGridScale'."""

    model_config = ConfigDict(protected_namespaces=())
