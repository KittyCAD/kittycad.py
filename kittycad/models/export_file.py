from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

YY = TypeVar("YY", bound="ExportFile")


@attr.s(auto_attribs=True)
class ExportFile:
    """A file to be exported to the client."""  # noqa: E501

    contents: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contents = self.contents
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[YY], src_dict: Dict[str, Any]) -> YY:
        d = src_dict.copy()
        contents = d.pop("contents", UNSET)

        name = d.pop("name", UNSET)

        export_file = cls(
            contents=contents,
            name=name,
        )

        export_file.additional_properties = d
        return export_file

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