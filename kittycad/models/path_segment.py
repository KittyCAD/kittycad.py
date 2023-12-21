from typing import Literal, Optional, Union

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated

from ..models.angle import Angle
from ..models.point2d import Point2d
from ..models.point3d import Point3d


class line(BaseModel):
    """A straight line segment. Goes from the current path "pen" to the given endpoint."""

    end: Point3d

    relative: bool

    type: Literal["line"] = "line"


class arc(BaseModel):
    """A circular arc segment."""

    center: Point2d

    end: Angle

    radius: float

    relative: bool

    start: Angle

    type: Literal["arc"] = "arc"


class bezier(BaseModel):
    """A cubic bezier curve segment. Start at the end of the current line, go through control point 1 and 2, then end at a given point."""

    control1: Point3d

    control2: Point3d

    end: Point3d

    relative: bool

    type: Literal["bezier"] = "bezier"


class tangential_arc(BaseModel):
    """Adds a tangent arc from current pen position with the given radius and angle."""

    offset: Angle

    radius: float

    type: Literal["tangential_arc"] = "tangential_arc"


class tangential_arc_to(BaseModel):
    """Adds a tangent arc from current pen position to the new position."""

    angle_snap_increment: Optional[Angle] = None

    to: Point3d

    type: Literal["tangential_arc_to"] = "tangential_arc_to"


PathSegment = RootModel[
    Annotated[
        Union[
            line,
            arc,
            bezier,
            tangential_arc,
            tangential_arc_to,
        ],
        Field(discriminator="type"),
    ]
]
