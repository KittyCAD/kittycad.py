from pydantic import BaseModel, ConfigDict


class Curvesetconstraint(BaseModel):
    """The response from the `CurveSetConstraint` endpoint."""

    model_config = ConfigDict(protected_namespaces=())
