from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

L = TypeVar("L", bound="Pong")


@attr.s(auto_attribs=True)
class Pong:
    """The response from the `/ping` endpoint."""  # noqa: E501

    message: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[L], src_dict: Dict[str, Any]) -> L:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        pong = cls(
            message=message,
        )

        pong.additional_properties = d
        return pong

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
