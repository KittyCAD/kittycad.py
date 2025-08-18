from typing import Optional

from ..models.transform_by_for_point3d import TransformByForPoint3d
from ..models.transform_by_for_point4d import TransformByForPoint4d
from .base import KittyCadBaseModel


class ComponentTransform(KittyCadBaseModel):
    """Container that holds a translate, rotate and scale. Defaults to no change, everything stays the same (i.e. the identity function)."""

    rotate_angle_axis: Optional[TransformByForPoint4d] = None

    rotate_rpy: Optional[TransformByForPoint3d] = None

    scale: Optional[TransformByForPoint3d] = None

    translate: Optional[TransformByForPoint3d] = None
