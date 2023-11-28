from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point3d import Point3d
from ..types import UNSET, Unset

DI = TypeVar("DI", bound="CurveGetEndPoints")


@attr.s(auto_attribs=True)
class CurveGetEndPoints:
    """Endpoints of a curve"""  # noqa: E501

    end: Union[Unset, Point3d] = UNSET
    start: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.end, Unset):
            end = self.end
        if not isinstance(self.start, Unset):
            start = self.start

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end.to_dict()
        if start is not UNSET:
            field_dict["start"] = start.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[DI], src_dict: Dict[str, Any]) -> DI:
        d = src_dict.copy()
        _end = d.pop("end", UNSET)
        end: Union[Unset, Point3d]
        if isinstance(_end, Unset):
            end = UNSET
        if _end is None:
            end = UNSET
        else:
            end = Point3d.from_dict(_end)

        _start = d.pop("start", UNSET)
        start: Union[Unset, Point3d]
        if isinstance(_start, Unset):
            start = UNSET
        if _start is None:
            start = UNSET
        else:
            start = Point3d.from_dict(_start)

        curve_get_end_points = cls(
            end=end,
            start=start,
        )

        curve_get_end_points.additional_properties = d
        return curve_get_end_points

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
