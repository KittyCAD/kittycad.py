from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

J = TypeVar("J", bound="EmailAuthenticationForm")


@attr.s(auto_attribs=True)
class EmailAuthenticationForm:
    """The body of the form for email authentication."""  # noqa: E501

    callback_url: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        callback_url = self.callback_url
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[J], src_dict: Dict[str, Any]) -> J:
        d = src_dict.copy()
        callback_url = d.pop("callback_url", UNSET)

        email = d.pop("email", UNSET)

        email_authentication_form = cls(
            callback_url=callback_url,
            email=email,
        )

        email_authentication_form.additional_properties = d
        return email_authentication_form

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
