import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

K = TypeVar("K", bound="VerificationToken")


@attr.s(auto_attribs=True)
class VerificationToken:
    """A verification token for a user.

    This is typically used to verify a user's email address."""  # noqa: E501

    created_at: Union[Unset, datetime.datetime] = UNSET
    expires: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()
        expires: Union[Unset, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()
        id = self.id
        identifier = self.identifier
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires is not UNSET:
            field_dict["expires"] = expires
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[K], src_dict: Dict[str, Any]) -> K:
        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _expires = d.pop("expires", UNSET)
        expires: Union[Unset, datetime.datetime]
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        verification_token = cls(
            created_at=created_at,
            expires=expires,
            id=id,
            identifier=identifier,
            updated_at=updated_at,
        )

        verification_token.additional_properties = d
        return verification_token

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
