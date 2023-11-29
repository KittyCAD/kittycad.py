
from pydantic import BaseModel

from ..models.curve_type import CurveType


class CurveGetType(BaseModel):
    """The response from the `CurveGetType` command."""

    curve_type: CurveType
