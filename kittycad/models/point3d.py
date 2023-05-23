from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

M = TypeVar("M", bound="Point3d")


@attr.s(auto_attribs=True)
class Point3d:
    """A point in 3D space"""  # noqa: E501

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    z: Union[Unset, float] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x = self.x
        y = self.y
        z = self.z

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: Type[M], src_dict: Dict[str, Any]) -> M:
        d = src_dict.copy()
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        z = d.pop("z", UNSET)

        point3d = cls(
            x=x,
            y=y,
            z=z,
        )

        point3d.additional_properties = d
        return point3d

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
