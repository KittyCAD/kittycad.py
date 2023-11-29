from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.angle import Angle
from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..types import UNSET, Unset

PM = TypeVar("PM", bound="line")


@attr.s(auto_attribs=True)
class line:
    """A straight line segment. Goes from the current path "pen" to the given endpoint."""  # noqa: E501

    end: Union[Unset, Point3d] = UNSET
    relative: Union[Unset, bool] = False
    type: str = "line"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end: Union[Unset, Point3d] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end
        relative = self.relative
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            _end: Point3d = cast(Point3d, end)
            field_dict["end"] = _end.to_dict()
        if relative is not UNSET:
            field_dict["relative"] = relative
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[PM], src_dict: Dict[str, Any]) -> PM:
        d = src_dict.copy()
        _end = d.pop("end", UNSET)
        end: Union[Unset, Point3d]
        if isinstance(_end, Unset):
            end = UNSET
        if _end is None:
            end = UNSET
        else:
            end = Point3d.from_dict(_end)

        relative = d.pop("relative", UNSET)

        type = d.pop("type", UNSET)

        line = cls(
            end=end,
            relative=relative,
            type=type,
        )

        line.additional_properties = d
        return line

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


HI = TypeVar("HI", bound="arc")


@attr.s(auto_attribs=True)
class arc:
    """A circular arc segment."""  # noqa: E501

    angle_end: Union[Unset, float] = UNSET
    angle_start: Union[Unset, float] = UNSET
    center: Union[Unset, Point2d] = UNSET
    end: Union[Unset, Angle] = UNSET
    radius: Union[Unset, float] = UNSET
    relative: Union[Unset, bool] = False
    start: Union[Unset, Angle] = UNSET
    type: str = "arc"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        angle_end = self.angle_end
        angle_start = self.angle_start
        center: Union[Unset, Point2d] = UNSET
        if not isinstance(self.center, Unset):
            center = self.center
        end: Union[Unset, Angle] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end
        radius = self.radius
        relative = self.relative
        start: Union[Unset, Angle] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angle_end is not UNSET:
            field_dict["angle_end"] = angle_end
        if angle_start is not UNSET:
            field_dict["angle_start"] = angle_start
        if center is not UNSET:
            _center: Point2d = cast(Point2d, center)
            field_dict["center"] = _center.to_dict()
        if end is not UNSET:
            _end: Angle = cast(Angle, end)
            field_dict["end"] = _end.to_dict()
        if radius is not UNSET:
            field_dict["radius"] = radius
        if relative is not UNSET:
            field_dict["relative"] = relative
        if start is not UNSET:
            _start: Angle = cast(Angle, start)
            field_dict["start"] = _start.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HI], src_dict: Dict[str, Any]) -> HI:
        d = src_dict.copy()
        angle_end = d.pop("angle_end", UNSET)

        angle_start = d.pop("angle_start", UNSET)

        _center = d.pop("center", UNSET)
        center: Union[Unset, Point2d]
        if isinstance(_center, Unset):
            center = UNSET
        if _center is None:
            center = UNSET
        else:
            center = Point2d.from_dict(_center)

        _end = d.pop("end", UNSET)
        end: Union[Unset, Angle]
        if isinstance(_end, Unset):
            end = UNSET
        if _end is None:
            end = UNSET
        else:
            end = Angle.from_dict(_end)

        radius = d.pop("radius", UNSET)

        relative = d.pop("relative", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, Angle]
        if isinstance(_start, Unset):
            start = UNSET
        if _start is None:
            start = UNSET
        else:
            start = Angle.from_dict(_start)

        type = d.pop("type", UNSET)

        arc = cls(
            angle_end=angle_end,
            angle_start=angle_start,
            center=center,
            end=end,
            radius=radius,
            relative=relative,
            start=start,
            type=type,
        )

        arc.additional_properties = d
        return arc

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


XD = TypeVar("XD", bound="bezier")


@attr.s(auto_attribs=True)
class bezier:
    """A cubic bezier curve segment. Start at the end of the current line, go through control point 1 and 2, then end at a given point."""  # noqa: E501

    control1: Union[Unset, Point3d] = UNSET
    control2: Union[Unset, Point3d] = UNSET
    end: Union[Unset, Point3d] = UNSET
    relative: Union[Unset, bool] = False
    type: str = "bezier"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        control1: Union[Unset, Point3d] = UNSET
        if not isinstance(self.control1, Unset):
            control1 = self.control1
        control2: Union[Unset, Point3d] = UNSET
        if not isinstance(self.control2, Unset):
            control2 = self.control2
        end: Union[Unset, Point3d] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end
        relative = self.relative
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control1 is not UNSET:
            _control1: Point3d = cast(Point3d, control1)
            field_dict["control1"] = _control1.to_dict()
        if control2 is not UNSET:
            _control2: Point3d = cast(Point3d, control2)
            field_dict["control2"] = _control2.to_dict()
        if end is not UNSET:
            _end: Point3d = cast(Point3d, end)
            field_dict["end"] = _end.to_dict()
        if relative is not UNSET:
            field_dict["relative"] = relative
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[XD], src_dict: Dict[str, Any]) -> XD:
        d = src_dict.copy()
        _control1 = d.pop("control1", UNSET)
        control1: Union[Unset, Point3d]
        if isinstance(_control1, Unset):
            control1 = UNSET
        if _control1 is None:
            control1 = UNSET
        else:
            control1 = Point3d.from_dict(_control1)

        _control2 = d.pop("control2", UNSET)
        control2: Union[Unset, Point3d]
        if isinstance(_control2, Unset):
            control2 = UNSET
        if _control2 is None:
            control2 = UNSET
        else:
            control2 = Point3d.from_dict(_control2)

        _end = d.pop("end", UNSET)
        end: Union[Unset, Point3d]
        if isinstance(_end, Unset):
            end = UNSET
        if _end is None:
            end = UNSET
        else:
            end = Point3d.from_dict(_end)

        relative = d.pop("relative", UNSET)

        type = d.pop("type", UNSET)

        bezier = cls(
            control1=control1,
            control2=control2,
            end=end,
            relative=relative,
            type=type,
        )

        bezier.additional_properties = d
        return bezier

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


HN = TypeVar("HN", bound="tangential_arc")


@attr.s(auto_attribs=True)
class tangential_arc:
    """Adds a tangent arc from current pen position with the given radius and angle."""  # noqa: E501

    offset: Union[Unset, Angle] = UNSET
    radius: Union[Unset, float] = UNSET
    type: str = "tangential_arc"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offset: Union[Unset, Angle] = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset
        radius = self.radius
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            _offset: Angle = cast(Angle, offset)
            field_dict["offset"] = _offset.to_dict()
        if radius is not UNSET:
            field_dict["radius"] = radius
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[HN], src_dict: Dict[str, Any]) -> HN:
        d = src_dict.copy()
        _offset = d.pop("offset", UNSET)
        offset: Union[Unset, Angle]
        if isinstance(_offset, Unset):
            offset = UNSET
        if _offset is None:
            offset = UNSET
        else:
            offset = Angle.from_dict(_offset)

        radius = d.pop("radius", UNSET)

        type = d.pop("type", UNSET)

        tangential_arc = cls(
            offset=offset,
            radius=radius,
            type=type,
        )

        tangential_arc.additional_properties = d
        return tangential_arc

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


OT = TypeVar("OT", bound="tangential_arc_to")


@attr.s(auto_attribs=True)
class tangential_arc_to:
    """Adds a tangent arc from current pen position to the new position."""  # noqa: E501

    angle_snap_increment: Union[Unset, Angle] = UNSET
    to: Union[Unset, Point3d] = UNSET
    type: str = "tangential_arc_to"

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        angle_snap_increment: Union[Unset, Angle] = UNSET
        if not isinstance(self.angle_snap_increment, Unset):
            angle_snap_increment = self.angle_snap_increment
        to: Union[Unset, Point3d] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angle_snap_increment is not UNSET:
            _angle_snap_increment: Angle = cast(Angle, angle_snap_increment)
            field_dict["angle_snap_increment"] = _angle_snap_increment.to_dict()
        if to is not UNSET:
            _to: Point3d = cast(Point3d, to)
            field_dict["to"] = _to.to_dict()
        field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[OT], src_dict: Dict[str, Any]) -> OT:
        d = src_dict.copy()
        _angle_snap_increment = d.pop("angle_snap_increment", UNSET)
        angle_snap_increment: Union[Unset, Angle]
        if isinstance(_angle_snap_increment, Unset):
            angle_snap_increment = UNSET
        if _angle_snap_increment is None:
            angle_snap_increment = UNSET
        else:
            angle_snap_increment = Angle.from_dict(_angle_snap_increment)

        _to = d.pop("to", UNSET)
        to: Union[Unset, Point3d]
        if isinstance(_to, Unset):
            to = UNSET
        if _to is None:
            to = UNSET
        else:
            to = Point3d.from_dict(_to)

        type = d.pop("type", UNSET)

        tangential_arc_to = cls(
            angle_snap_increment=angle_snap_increment,
            to=to,
            type=type,
        )

        tangential_arc_to.additional_properties = d
        return tangential_arc_to

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


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

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.type, line):
            AT: line = self.type
            return AT.to_dict()
        elif isinstance(self.type, arc):
            KI: arc = self.type
            return KI.to_dict()
        elif isinstance(self.type, bezier):
            HW: bezier = self.type
            return HW.to_dict()
        elif isinstance(self.type, tangential_arc):
            FR: tangential_arc = self.type
            return FR.to_dict()
        elif isinstance(self.type, tangential_arc_to):
            WZ: tangential_arc_to = self.type
            return WZ.to_dict()

        raise Exception("Unknown type")

    @classmethod
    def from_dict(cls: Type[GY], d: Dict[str, Any]) -> GY:
        if d.get("type") == "line":
            GF: line = line()
            GF.from_dict(d)
            return cls(type=GF)
        elif d.get("type") == "arc":
            RM: arc = arc()
            RM.from_dict(d)
            return cls(type=RM)
        elif d.get("type") == "bezier":
            UD: bezier = bezier()
            UD.from_dict(d)
            return cls(type=UD)
        elif d.get("type") == "tangential_arc":
            GT: tangential_arc = tangential_arc()
            GT.from_dict(d)
            return cls(type=GT)
        elif d.get("type") == "tangential_arc_to":
            BQ: tangential_arc_to = tangential_arc_to()
            BQ.from_dict(d)
            return cls(type=BQ)

        raise Exception("Unknown type")
