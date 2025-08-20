from .base import KittyCadBaseModel


class PathGetCurveUuid(KittyCadBaseModel):
    """The response from the `PathGetCurveUuid` command."""

    curve_id: str
