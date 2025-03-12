from typing import List

from pydantic import BaseModel, ConfigDict

from ..models.world_coordinate_system import WorldCoordinateSystem


class CameraViewState(BaseModel):
    """"""

    eye_offset: float

    fov_y: float

    is_ortho: bool

    ortho_scale_enabled: bool

    ortho_scale_factor: float

    pivot_position: List[float]

    pivot_rotation: List[float]

    world_coord_system: WorldCoordinateSystem

    model_config = ConfigDict(protected_namespaces=())
