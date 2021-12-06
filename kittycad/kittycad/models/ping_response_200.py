from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ping_response_200_message import PingResponse200Message
from ..types import UNSET, Unset

T = TypeVar("T", bound="PingResponse200")


@attr.s(auto_attribs=True)
class PingResponse200:
    """ """

    message: Union[Unset, PingResponse200Message] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message: Union[Unset, str] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _message = d.pop("message", UNSET)
        message: Union[Unset, PingResponse200Message]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = PingResponse200Message(_message)

        ping_response_200 = cls(
            message=message,
        )

        ping_response_200.additional_properties = d
        return ping_response_200

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
