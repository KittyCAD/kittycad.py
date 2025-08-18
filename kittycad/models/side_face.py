from .base import KittyCadBaseModel


class SideFace(KittyCadBaseModel):
    """IDs for a side face, extruded from the path of some sketch/2D shape."""

    face_id: str

    path_id: str
