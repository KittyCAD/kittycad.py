from pydantic import BaseModel, ConfigDict


class Objectsetmaterialparamspbr(BaseModel):
    """The response from the `ObjectSetMaterialParamsPbr` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
