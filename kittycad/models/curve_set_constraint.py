from pydantic import BaseModel, ConfigDict


class CurveSetConstraint(BaseModel):
    """The response from the `CurveSetConstraint` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
