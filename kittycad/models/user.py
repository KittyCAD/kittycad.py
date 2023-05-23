import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

W = TypeVar("W", bound="User")


@attr.s(auto_attribs=True)
class User:
    """A user."""  # noqa: E501

    company: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    discord: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    email_verified: Union[Unset, datetime.datetime] = UNSET
    first_name: Union[Unset, str] = UNSET
    github: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company = self.company
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        discord = self.discord
        email = self.email
        email_verified: Union[Unset, str] = UNSET
        if not isinstance(self.email_verified, Unset):
            email_verified = self.email_verified.isoformat()
        first_name = self.first_name
        github = self.github
        id = self.id
        image = self.image
        last_name = self.last_name
        name = self.name
        phone = self.phone
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if discord is not UNSET:
            field_dict["discord"] = discord
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if github is not UNSET:
            field_dict["github"] = github
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[W], src_dict: Dict[str, Any]) -> W:
        d = src_dict.copy()
        company = d.pop("company", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        discord = d.pop("discord", UNSET)

        email = d.pop("email", UNSET)

        _email_verified = d.pop("email_verified", UNSET)
        email_verified: Union[Unset, datetime.datetime]
        if isinstance(_email_verified, Unset):
            email_verified = UNSET
        else:
            email_verified = isoparse(_email_verified)

        first_name = d.pop("first_name", UNSET)

        github = d.pop("github", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        last_name = d.pop("last_name", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user = cls(
            company=company,
            created_at=created_at,
            discord=discord,
            email=email,
            email_verified=email_verified,
            first_name=first_name,
            github=github,
            id=id,
            image=image,
            last_name=last_name,
            name=name,
            phone=phone,
            updated_at=updated_at,
        )

        user.additional_properties = d
        return user

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
