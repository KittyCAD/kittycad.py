from pydantic import BaseModel, ConfigDict


class Entitymakehelix(BaseModel):
    """The response from the `EntityMakeHelix` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
