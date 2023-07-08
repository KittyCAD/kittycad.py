from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point2d import Point2d
from ..models.point3d import Point3d
from ..types import UNSET, Unset

F = TypeVar("F", bound="Line")


@attr.s(auto_attribs=True)
class Line:
    end: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.end, Unset):
            end = self.end

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[F], src_dict: Dict[str, Any]) -> F:
        d = src_dict.copy()
        _end = d.pop("end", UNSET)
        end: Union[Unset, Point3d]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = Point3d(_end)

        line = cls(
            end=end,
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


Z = TypeVar("Z", bound="Arc")


@attr.s(auto_attribs=True)
class Arc:
    angle_end: Union[Unset, float] = UNSET
    angle_start: Union[Unset, float] = UNSET
    center: Union[Unset, Point2d] = UNSET
    radius: Union[Unset, float] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        angle_end = self.angle_end
        angle_start = self.angle_start
        if not isinstance(self.center, Unset):
            center = self.center
        radius = self.radius

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angle_end is not UNSET:
            field_dict["angle_end"] = angle_end
        if angle_start is not UNSET:
            field_dict["angle_start"] = angle_start
        if center is not UNSET:
            field_dict["center"] = center
        if radius is not UNSET:
            field_dict["radius"] = radius

        return field_dict

    @classmethod
    def from_dict(cls: Type[Z], src_dict: Dict[str, Any]) -> Z:
        d = src_dict.copy()
        angle_end = d.pop("angle_end", UNSET)

        angle_start = d.pop("angle_start", UNSET)

        _center = d.pop("center", UNSET)
        center: Union[Unset, Point2d]
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = Point2d(_center)

        radius = d.pop("radius", UNSET)

        arc = cls(
            angle_end=angle_end,
            angle_start=angle_start,
            center=center,
            radius=radius,
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


G = TypeVar("G", bound="Bezier")


@attr.s(auto_attribs=True)
class Bezier:
    control1: Union[Unset, Point3d] = UNSET
    control2: Union[Unset, Point3d] = UNSET
    end: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.control1, Unset):
            control1 = self.control1
        if not isinstance(self.control2, Unset):
            control2 = self.control2
        if not isinstance(self.end, Unset):
            end = self.end

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control1 is not UNSET:
            field_dict["control1"] = control1
        if control2 is not UNSET:
            field_dict["control2"] = control2
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[G], src_dict: Dict[str, Any]) -> G:
        d = src_dict.copy()
        _control1 = d.pop("control1", UNSET)
        control1: Union[Unset, Point3d]
        if isinstance(_control1, Unset):
            control1 = UNSET
        else:
            control1 = Point3d(_control1)

        _control2 = d.pop("control2", UNSET)
        control2: Union[Unset, Point3d]
        if isinstance(_control2, Unset):
            control2 = UNSET
        else:
            control2 = Point3d(_control2)

        _end = d.pop("end", UNSET)
        end: Union[Unset, Point3d]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = Point3d(_end)

        bezier = cls(
            control1=control1,
            control2=control2,
            end=end,
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


PathSegment = Union[Line, Arc, Bezier]
