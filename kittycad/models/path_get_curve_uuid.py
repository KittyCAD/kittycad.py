
from pydantic import BaseModel, ConfigDict



class PathGetCurveUuid(BaseModel):
    """The response from the `PathGetCurveUuid` command."""

    curve_id: str

    model_config = ConfigDict(protected_namespaces=())
