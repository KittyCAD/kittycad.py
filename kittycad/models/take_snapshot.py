from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.base64data import Base64Data
from ..types import UNSET, Unset

QT = TypeVar("QT", bound="TakeSnapshot")


@attr.s(auto_attribs=True)
class TakeSnapshot:
    """The response from the `TakeSnapshot` command."""  # noqa: E501

    contents: Union[Unset, Base64Data] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contents: Union[Unset, str] = UNSET
        if not isinstance(self.contents, Unset):
            contents = self.contents.get_encoded()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: Type[QT], src_dict: Dict[str, Any]) -> QT:
        d = src_dict.copy()
        _contents = d.pop("contents", UNSET)
        contents: Union[Unset, Base64Data]
        if isinstance(_contents, Unset):
            contents = UNSET
        else:
            contents = Base64Data(bytes(_contents, "utf-8"))

        take_snapshot = cls(
            contents=contents,
        )

        take_snapshot.additional_properties = d
        return take_snapshot

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