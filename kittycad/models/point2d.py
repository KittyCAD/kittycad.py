from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

E = TypeVar("E", bound="Point2d")


@attr.s(auto_attribs=True)
class Point2d:
    """A point in 2D space"""  # noqa: E501

    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        x = self.x
        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[E], src_dict: Dict[str, Any]) -> E:
        d = src_dict.copy()
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        point2d = cls(
            x=x,
            y=y,
        )

        point2d.additional_properties = d
        return point2d

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
