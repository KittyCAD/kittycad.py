from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

R = TypeVar("R", bound="IndexInfo")


@attr.s(auto_attribs=True)
class IndexInfo:
    """IndexInfo contains information about a registry."""  # noqa: E501

    mirrors: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    official: Union[Unset, bool] = False
    secure: Union[Unset, bool] = False

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mirrors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mirrors, Unset):
            mirrors = self.mirrors
        name = self.name
        official = self.official
        secure = self.secure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mirrors is not UNSET:
            field_dict["mirrors"] = mirrors
        if name is not UNSET:
            field_dict["name"] = name
        if official is not UNSET:
            field_dict["official"] = official
        if secure is not UNSET:
            field_dict["secure"] = secure

        return field_dict

    @classmethod
    def from_dict(cls: Type[R], src_dict: Dict[str, Any]) -> R:
        d = src_dict.copy()
        mirrors = cast(List[str], d.pop("mirrors", UNSET))

        name = d.pop("name", UNSET)

        official = d.pop("official", UNSET)

        secure = d.pop("secure", UNSET)

        index_info = cls(
            mirrors=mirrors,
            name=name,
            official=official,
            secure=secure,
        )

        index_info.additional_properties = d
        return index_info

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
