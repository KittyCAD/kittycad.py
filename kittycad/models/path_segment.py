from typing import Any, Dict, Optional, Type, TypeVar, Union

import attr
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

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


GY = TypeVar("GY", bound="PathSegment")


@attr.s(auto_attribs=True)
class PathSegment:

    """A segment of a path. Paths are composed of many segments."""

    type: Union[
        line,
        arc,
        bezier,
        tangential_arc,
        tangential_arc_to,
    ]

    def __init__(
        self,
        type: Union[
            line,
            arc,
            bezier,
            tangential_arc,
            tangential_arc_to,
        ],
    ):
        self.type = type

    def model_dump(self) -> Dict[str, Any]:
        if isinstance(self.type, line):
            EW: line = self.type
            return EW.model_dump()
        elif isinstance(self.type, arc):
            BT: arc = self.type
            return BT.model_dump()
        elif isinstance(self.type, bezier):
            AG: bezier = self.type
            return AG.model_dump()
        elif isinstance(self.type, tangential_arc):
            EA: tangential_arc = self.type
            return EA.model_dump()
        elif isinstance(self.type, tangential_arc_to):
            VW: tangential_arc_to = self.type
            return VW.model_dump()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "line":
            BU: line = line(**d)
            return cls(type=BU)
        elif d.get("type") == "arc":
            GR: arc = arc(**d)
            return cls(type=GR)
        elif d.get("type") == "bezier":
            EJ: bezier = bezier(**d)
            return cls(type=EJ)
        elif d.get("type") == "tangential_arc":
            LQ: tangential_arc = tangential_arc(**d)
            return cls(type=LQ)
        elif d.get("type") == "tangential_arc_to":
            DP: tangential_arc_to = tangential_arc_to(**d)
            return cls(type=DP)

        raise Exception("Unknown type")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls,
            handler(
                Union[
                    line,
                    arc,
                    bezier,
                    tangential_arc,
                    tangential_arc_to,
                ]
            ),
        )
