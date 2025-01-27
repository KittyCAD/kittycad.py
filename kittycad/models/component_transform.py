from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.transform_by_for_point3d import TransformByForPoint3d
from ..models.transform_by_for_point4d import TransformByForPoint4d


class ComponentTransform(BaseModel):
    """Container that holds a translate, rotate and scale."""

    rotate_angle_axis: Optional[TransformByForPoint4d] = None

    rotate_rpy: Optional[TransformByForPoint3d] = None

    scale: Optional[TransformByForPoint3d] = None

    translate: Optional[TransformByForPoint3d] = None

    model_config = ConfigDict(protected_namespaces=())
