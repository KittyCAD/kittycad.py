from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point3d import Point3d
from ..types import UNSET, Unset

P = TypeVar("P", bound="Line3d")


@attr.s(auto_attribs=True)
class Line3d:
    """Command for adding a line."""  # noqa: E501

    from_: Union[Unset, Point3d] = UNSET
    to: Union[Unset, Point3d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.from_, Unset):
            from_ = self.from_
        if not isinstance(self.to, Unset):
            to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[P], src_dict: Dict[str, Any]) -> P:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, Point3d]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = Point3d(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, Point3d]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Point3d(_to)

        line3d = cls(
            from_=from_,
            to=to,
        )

        line3d.additional_properties = d
        return line3d

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
