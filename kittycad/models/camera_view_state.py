from pydantic import BaseModel, ConfigDict

from ..models.point3d import Point3d
from ..models.point4d import Point4d
from ..models.world_coordinate_system import WorldCoordinateSystem


class CameraViewState(BaseModel):
    """"""

    eye_offset: float

    fov_y: float

    is_ortho: bool

    ortho_scale_enabled: bool

    ortho_scale_factor: float

    pivot_position: Point3d

    pivot_rotation: Point4d

    world_coord_system: WorldCoordinateSystem

    model_config = ConfigDict(protected_namespaces=())
