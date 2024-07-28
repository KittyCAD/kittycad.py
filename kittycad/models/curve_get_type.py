
from pydantic import BaseModel, ConfigDict

from ..models.curve_type import CurveType


class CurveGetType(BaseModel):
    """The response from the `CurveGetType` command."""

    curve_type: CurveType

    model_config = ConfigDict(protected_namespaces=())
