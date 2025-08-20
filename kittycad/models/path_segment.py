from typing import Literal, Optional, Union

from pydantic import Field, RootModel
from typing_extensions import Annotated

from ..models.angle import Angle
from ..models.length_unit import LengthUnit
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from .base import KittyCadBaseModel


class OptionLine(KittyCadBaseModel):
    """A straight line segment. Goes from the current path \"pen\" to the given endpoint."""

    end: Point3d

    relative: bool

    type: Literal["line"] = "line"


class OptionArc(KittyCadBaseModel):
    """A circular arc segment. Arcs can be drawn clockwise when start > end."""

    center: Point2d

    end: Angle

    radius: LengthUnit

    relative: bool

    start: Angle

    type: Literal["arc"] = "arc"


class OptionBezier(KittyCadBaseModel):
    """A cubic bezier curve segment. Start at the end of the current line, go through control point 1 and 2, then end at a given point."""

    control1: Point3d

    control2: Point3d

    end: Point3d

    relative: bool

    type: Literal["bezier"] = "bezier"


class OptionTangentialArc(KittyCadBaseModel):
    """Adds a tangent arc from current pen position with the given radius and angle."""

    offset: Angle

    radius: LengthUnit

    type: Literal["tangential_arc"] = "tangential_arc"


class OptionTangentialArcTo(KittyCadBaseModel):
    """Adds a tangent arc from current pen position to the new position. Arcs will choose a clockwise or counter-clockwise direction based on the arc end position."""

    angle_snap_increment: Optional[Angle] = None

    to: Point3d

    type: Literal["tangential_arc_to"] = "tangential_arc_to"


class OptionArcTo(KittyCadBaseModel):
    """Adds an arc from the current position that goes through the given interior point and ends at the given end position"""

    end: Point3d

    interior: Point3d

    relative: bool

    type: Literal["arc_to"] = "arc_to"


class OptionCircularInvolute(KittyCadBaseModel):
    """Adds a circular involute from the current position that goes through the given end_radius and is rotated around the current point by angle."""

    angle: Angle

    end_radius: LengthUnit

    reverse: bool

    start_radius: LengthUnit

    type: Literal["circular_involute"] = "circular_involute"


class OptionEllipse(KittyCadBaseModel):
    """Adds an elliptical arc segment."""

    center: Point2d

    end_angle: Angle

    major_axis: Point2d

    minor_radius: LengthUnit

    start_angle: Angle

    type: Literal["ellipse"] = "ellipse"


class OptionConicTo(KittyCadBaseModel):
    """Adds a generic conic section specified by the end point, interior point and tangents at the start and end of the section."""

    end: Point2d

    end_tangent: Point2d

    interior: Point2d

    relative: bool

    start_tangent: Point2d

    type: Literal["conic_to"] = "conic_to"


PathSegment = RootModel[
    Annotated[
        Union[
            OptionLine,
            OptionArc,
            OptionBezier,
            OptionTangentialArc,
            OptionTangentialArcTo,
            OptionArcTo,
            OptionCircularInvolute,
            OptionEllipse,
            OptionConicTo,
        ],
        Field(discriminator="type"),
    ]
]
