from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pong_enum import PongEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PongMessage")


@attr.s(auto_attribs=True)
class PongMessage:
    """ """
    message: Union[Unset, PongEnum] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message: Union[Unset, str] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict['message'] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _message = d.pop("message", UNSET)
        message: Union[Unset, PongEnum]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = PongEnum(_message)

        pong_message = cls(
            message=message,
        )

        pong_message.additional_properties = d
        return pong_message

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
