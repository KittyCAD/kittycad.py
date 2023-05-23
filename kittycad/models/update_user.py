from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

R = TypeVar("R", bound="UpdateUser")


@attr.s(auto_attribs=True)
class UpdateUser:
    """The user-modifiable parts of a User."""  # noqa: E501

    company: Union[Unset, str] = UNSET
    discord: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    github: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company = self.company
        discord = self.discord
        first_name = self.first_name
        github = self.github
        last_name = self.last_name
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if discord is not UNSET:
            field_dict["discord"] = discord
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if github is not UNSET:
            field_dict["github"] = github
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[R], src_dict: Dict[str, Any]) -> R:
        d = src_dict.copy()
        company = d.pop("company", UNSET)

        discord = d.pop("discord", UNSET)

        first_name = d.pop("first_name", UNSET)

        github = d.pop("github", UNSET)

        last_name = d.pop("last_name", UNSET)

        phone = d.pop("phone", UNSET)

        update_user = cls(
            company=company,
            discord=discord,
            first_name=first_name,
            github=github,
            last_name=last_name,
            phone=phone,
        )

        update_user.additional_properties = d
        return update_user

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
