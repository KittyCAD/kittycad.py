from typing import List

from ..models.modeling_cmd_id import ModelingCmdId
from ..models.point3d import Point3d
from ..models.projection import Projection
from ..models.visibility import Visibility
from .base import KittyCadBaseModel


class NamedView(KittyCadBaseModel):
    """Options for exporting glTF 2.0."""

    baseline: Visibility

    except_ids: List[ModelingCmdId]

    projection: Projection

    target: Point3d

    up: Point3d

    vantage: Point3d
