from .base import KittyCadBaseModel


class Solid3dGetFaceUuid(KittyCadBaseModel):
    """The response from the `Solid3dGetFaceUuid` endpoint."""

    face_id: str
