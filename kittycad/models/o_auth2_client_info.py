from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

B = TypeVar("B", bound="OAuth2ClientInfo")


@attr.s(auto_attribs=True)
class OAuth2ClientInfo:
    """Information about an OAuth 2.0 client."""  # noqa: E501

    csrf_token: Union[Unset, str] = UNSET
    pkce_code_verifier: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        csrf_token = self.csrf_token
        pkce_code_verifier = self.pkce_code_verifier
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csrf_token is not UNSET:
            field_dict["csrf_token"] = csrf_token
        if pkce_code_verifier is not UNSET:
            field_dict["pkce_code_verifier"] = pkce_code_verifier
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[B], src_dict: Dict[str, Any]) -> B:
        d = src_dict.copy()
        csrf_token = d.pop("csrf_token", UNSET)

        pkce_code_verifier = d.pop("pkce_code_verifier", UNSET)

        url = d.pop("url", UNSET)

        o_auth2_client_info = cls(
            csrf_token=csrf_token,
            pkce_code_verifier=pkce_code_verifier,
            url=url,
        )

        o_auth2_client_info.additional_properties = d
        return o_auth2_client_info

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
