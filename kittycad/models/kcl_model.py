from .base import KittyCadBaseModel


class KclModel(KittyCadBaseModel):
    """The response containing the KCL code."""

    code: str
