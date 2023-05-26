from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.point2d import Point2d
from ..types import UNSET, Unset
from .extrude import Extrude
from .line3d import Line3d

AddLine = Line3d


K = TypeVar("K", bound="SelectionClick")


@attr.s(auto_attribs=True)
class SelectionClick:
    at: Union[Unset, Point2d] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if not isinstance(self.at, Unset):
            at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[K], src_dict: Dict[str, Any]) -> K:
        d = src_dict.copy()
        _at = d.pop("at", UNSET)
        at: Union[Unset, Point2d]
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = Point2d(_at)

        selection_click = cls(
            at=at,
        )

        selection_click.additional_properties = d
        return selection_click

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


ModelingCmd = Union[AddLine, Extrude, SelectionClick]
