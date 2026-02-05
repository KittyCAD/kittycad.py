from ..models.body_type import BodyType
from .base import KittyCadBaseModel


class Solid3dGetBodyType(KittyCadBaseModel):
    """The response from the `Solid3dGetBodyType` endpoint."""

    body_type: BodyType
