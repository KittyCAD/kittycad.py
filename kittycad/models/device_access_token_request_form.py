from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.o_auth2_grant_type import OAuth2GrantType
from ..types import UNSET, Unset

J = TypeVar("J", bound="DeviceAccessTokenRequestForm")


@attr.s(auto_attribs=True)
class DeviceAccessTokenRequestForm:
    """The form for a device access token request."""  # noqa: E501

    client_id: Union[Unset, str] = UNSET
    device_code: Union[Unset, str] = UNSET
    grant_type: Union[Unset, OAuth2GrantType] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        device_code = self.device_code
        if not isinstance(self.grant_type, Unset):
            grant_type = self.grant_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if device_code is not UNSET:
            field_dict["device_code"] = device_code
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[J], src_dict: Dict[str, Any]) -> J:
        d = src_dict.copy()
        client_id = d.pop("client_id", UNSET)

        device_code = d.pop("device_code", UNSET)

        _grant_type = d.pop("grant_type", UNSET)
        grant_type: Union[Unset, OAuth2GrantType]
        if isinstance(_grant_type, Unset):
            grant_type = UNSET
        else:
            grant_type = OAuth2GrantType(_grant_type)

        device_access_token_request_form = cls(
            client_id=client_id,
            device_code=device_code,
            grant_type=grant_type,
        )

        device_access_token_request_form.additional_properties = d
        return device_access_token_request_form

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
