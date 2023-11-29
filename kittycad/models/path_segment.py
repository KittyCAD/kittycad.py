from typing import Optional, Union

from pydantic import BaseModel, RootModel

from ..models.angle import Angle
from ..models.point2d import Point2d
from ..models.point3d import Point3d


class line(BaseModel):
    """A straight line segment. Goes from the current path "pen" to the given endpoint."""

    end: Point3d

    relative: bool

    type: str = "line"


class arc(BaseModel):
    """A circular arc segment."""

    angle_end: float

    angle_start: float

    center: Point2d

    end: Optional[Angle] = None

    radius: float

    relative: bool

    start: Optional[Angle] = None

    type: str = "arc"


class bezier(BaseModel):
    """A cubic bezier curve segment. Start at the end of the current line, go through control point 1 and 2, then end at a given point."""

    control1: Point3d

    control2: Point3d

    end: Point3d

    relative: bool

    type: str = "bezier"


class tangential_arc(BaseModel):
    """Adds a tangent arc from current pen position with the given radius and angle."""

    offset: Angle

    radius: float

    type: str = "tangential_arc"


class tangential_arc_to(BaseModel):
    """Adds a tangent arc from current pen position to the new position."""

    angle_snap_increment: Optional[Angle] = None

    to: Point3d

    type: str = "tangential_arc_to"


PathSegment = RootModel[
    Union[
        line,
        arc,
        bezier,
        tangential_arc,
        tangential_arc_to,
    ]
]
