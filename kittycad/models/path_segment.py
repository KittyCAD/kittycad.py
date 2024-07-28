from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.angle import Angle
from ..models.length_unit import LengthUnit
from ..models.point2d import Point2d
from ..models.point3d import Point3d


class line(BaseModel):
    """A straight line segment. Goes from the current path \"pen\" to the given endpoint."""

    end: Point3d

    relative: bool

    type: Literal["line"] = "line"

    model_config = ConfigDict(protected_namespaces=())


class arc(BaseModel):
    """A circular arc segment. Arcs can be drawn clockwise when start > end."""

    center: Point2d

    end: Angle

    radius: LengthUnit

    relative: bool

    start: Angle

    type: Literal["arc"] = "arc"

    model_config = ConfigDict(protected_namespaces=())


class bezier(BaseModel):
    """A cubic bezier curve segment. Start at the end of the current line, go through control point 1 and 2, then end at a given point."""

    control1: Point3d

    control2: Point3d

    end: Point3d

    relative: bool

    type: Literal["bezier"] = "bezier"

    model_config = ConfigDict(protected_namespaces=())


class tangential_arc(BaseModel):
    """Adds a tangent arc from current pen position with the given radius and angle."""

    offset: Angle

    radius: LengthUnit

    type: Literal["tangential_arc"] = "tangential_arc"

    model_config = ConfigDict(protected_namespaces=())


class tangential_arc_to(BaseModel):
    """Adds a tangent arc from current pen position to the new position. Arcs will choose a clockwise or counter-clockwise direction based on the arc end position."""

    angle_snap_increment: Optional[Angle] = None

    to: Point3d

    type: Literal["tangential_arc_to"] = "tangential_arc_to"

    model_config = ConfigDict(protected_namespaces=())


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
