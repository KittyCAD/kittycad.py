from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated

from ..models.angle import Angle
from ..models.length_unit import LengthUnit
from ..models.point2d import Point2d
from ..models.point3d import Point3d


class OptionLine(BaseModel):
    """A straight line segment. Goes from the current path \"pen\" to the given endpoint."""

    end: Point3d

    relative: bool

    type: Literal["line"] = "line"

    model_config = ConfigDict(protected_namespaces=())


class OptionArc(BaseModel):
    """A circular arc segment. Arcs can be drawn clockwise when start > end."""

    center: Point2d

    end: Angle

    radius: LengthUnit

    relative: bool

    start: Angle

    type: Literal["arc"] = "arc"

    model_config = ConfigDict(protected_namespaces=())


class OptionBezier(BaseModel):
    """A cubic bezier curve segment. Start at the end of the current line, go through control point 1 and 2, then end at a given point."""

    control1: Point3d

    control2: Point3d

    end: Point3d

    relative: bool

    type: Literal["bezier"] = "bezier"

    model_config = ConfigDict(protected_namespaces=())


class OptionTangentialArc(BaseModel):
    """Adds a tangent arc from current pen position with the given radius and angle."""

    offset: Angle

    radius: LengthUnit

    type: Literal["tangential_arc"] = "tangential_arc"

    model_config = ConfigDict(protected_namespaces=())


class OptionTangentialArcTo(BaseModel):
    """Adds a tangent arc from current pen position to the new position. Arcs will choose a clockwise or counter-clockwise direction based on the arc end position."""

    angle_snap_increment: Optional[Angle] = None

    to: Point3d

    type: Literal["tangential_arc_to"] = "tangential_arc_to"

    model_config = ConfigDict(protected_namespaces=())


class OptionArcTo(BaseModel):
    """Adds an arc from the current position that goes through the given interior point and ends at the given end position"""

    end: Point3d

    interior: Point3d

    relative: bool

    type: Literal["arc_to"] = "arc_to"

    model_config = ConfigDict(protected_namespaces=())


class OptionCircularInvolute(BaseModel):
    """Adds a circular involute from the current position that goes through the given end_radius and is rotated around the current point by angle."""

    angle: Angle

    end_radius: LengthUnit

    reverse: bool

    start_radius: LengthUnit

    type: Literal["circular_involute"] = "circular_involute"

    model_config = ConfigDict(protected_namespaces=())


class OptionEllipse(BaseModel):
    """Adds an elliptical arc segment."""

    center: Point2d

    end_angle: Angle

    major_axis: Point2d

    minor_radius: LengthUnit

    start_angle: Angle

    type: Literal["ellipse"] = "ellipse"

    model_config = ConfigDict(protected_namespaces=())


class OptionConicTo(BaseModel):
    """Adds a generic conic section specified by the end point, interior point and tangents at the start and end of the section."""

    end: Point2d

    end_tangent: Point2d

    interior: Point2d

    relative: bool

    start_tangent: Point2d

    type: Literal["conic_to"] = "conic_to"

    model_config = ConfigDict(protected_namespaces=())


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
