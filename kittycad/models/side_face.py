from pydantic import BaseModel, ConfigDict


class SideFace(BaseModel):
    """IDs for a side face, extruded from the path of some sketch/2D shape."""

    face_id: str

    path_id: str

    model_config = ConfigDict(protected_namespaces=())
