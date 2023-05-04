from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

F = TypeVar("F", bound="DeviceAuthVerifyParams")


@attr.s(auto_attribs=True)
class DeviceAuthVerifyParams:
    """The request parameters to verify the `user_code` for the OAuth 2.0 Device Authorization Grant."""  # noqa: E501

    user_code: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_code = self.user_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_code is not UNSET:
            field_dict["user_code"] = user_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[F], src_dict: Dict[str, Any]) -> F:
        d = src_dict.copy()
        user_code = d.pop("user_code", UNSET)

        device_auth_verify_params = cls(
            user_code=user_code,
        )

        device_auth_verify_params.additional_properties = d
        return device_auth_verify_params

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
