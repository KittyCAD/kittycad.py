from pydantic import BaseModel, ConfigDict


class Kclmodel(BaseModel):
    """The response containing the KCL code."""

    code: str

    model_config = ConfigDict(protected_namespaces=())
