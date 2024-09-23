from pydantic import BaseModel, ConfigDict


class ObjectSetMaterialParamsPbr(BaseModel):
    """The response from the `ObjectSetMaterialParamsPbr` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
