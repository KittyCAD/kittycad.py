from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

V = TypeVar("V", bound="DeviceAuthRequestForm")


@attr.s(auto_attribs=True)
class DeviceAuthRequestForm:
    """The request parameters for the OAuth 2.0 Device Authorization Grant flow."""  # noqa: E501

    client_id: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[V], src_dict: Dict[str, Any]) -> V:
        d = src_dict.copy()
        client_id = d.pop("client_id", UNSET)

        device_auth_request_form = cls(
            client_id=client_id,
        )

        device_auth_request_form.additional_properties = d
        return device_auth_request_form

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
